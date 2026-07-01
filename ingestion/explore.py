import pandas as pd
from pathlib import Path

DATA_DIR = Path("/Users/tylerreinders/projects/tennis_atp")
TOP_N = 10

def load_all_matches(data_dir: Path) -> pd.DataFrame:
    """
    Takes atp matches from every year and combines them into one data frame

    Args:
        data_dir: filepath to file of atp match data from every year
    
    Returns:
        Data frame of matches from every year
    """
    files = sorted(data_dir.glob("atp_matches_[0-9][0-9][0-9][0-9].csv"))
    data_frames = [pd.read_csv(f) for f in files]
    all_matches = pd.concat(data_frames, ignore_index = True)
    return all_matches

def display_shape(matches: pd.DataFrame) -> None:
    """
    Prints the rows and columns for the data frame of all atp matches

    Args:
        matches: data frame of all match data

    Returns:
        None
    """
    print(f"Shape: {matches.shape}")

def display_column_names(matches: pd.DataFrame) -> None:
    """
    Prints each column name of data in the data frame of atp matches

    Args:
        matches: data frame of all match data

    Returns:
        None
    """
    print(f"Column names: {matches.columns}")

def format_date(matches: pd.DataFrame) -> pd.DataFrame:
    """
    Formats the integers in date column into year, month, day

    Args:
        matches: data frame of all match data

    Returns:
        data frame of all atp matches with tournament date column converted to year, month, day
    """
    matches['tourney_date'] = pd.to_datetime(matches['tourney_date'], format='%Y%m%d')
    return matches

def display_date_ranges(matches: pd.DataFrame) -> None:
    """
    Prints the earliest and most recent match date

    Args:
        matches: data frame of all match data

    Returns:
        None
    """
    print(f"the earliest match date is {matches['tourney_date'].min()}")
    print(f"the most recent match date is {matches['tourney_date'].max()}")

def report_missingness(matches: pd.DataFrame) -> None:
    """
    Prints the total amount of missing data values per column

    Args:
        matches: data frame of all match data

    Returns:
        None
    """
    print(f"The number of missing data values in each column are:\n{matches.isna().sum()}")

def get_top_players(matches: pd.DataFrame, n: int = TOP_N) -> pd.DataFrame:
    """
    Creates a data frame of a given number of players with the most appearances listed in descending order

    Args:
        matches: data frame of all match data
        n: number of players and player appearances to be listed in the returned data frame

    Returns:
        Data frame with players that have the most appearances, listed in descending order
    """
    winners = matches[['winner_name', 'winner_rank', 'surface', 'tourney_date']].rename(
        columns={'winner_name': 'player_name', 'winner_rank': 'player_rank'})
    winners["won"] = True
    losers = matches[['loser_name', 'loser_rank', 'surface', 'tourney_date']].rename(
        columns={'loser_name': 'player_name', 'loser_rank': 'player_rank'})
    losers["won"] = False
    player_matches = pd.concat([winners, losers], ignore_index = True)
    top = player_matches.groupby('player_name').size().sort_values(ascending=False).head(n).reset_index(name='appearances')
    top.index = range(1, len(top) + 1)
    return top

def main() -> None:
    matches = load_all_matches(DATA_DIR)
    display_shape(matches)
    display_column_names(matches)
    matches = format_date(matches)
    display_date_ranges(matches)
    report_missingness(matches)
    print(get_top_players(matches))

if __name__ == "__main__":
    main()