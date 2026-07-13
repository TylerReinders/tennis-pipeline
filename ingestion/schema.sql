CREATE TABLE players (
    player_id INTEGER PRIMARY KEY,
    name_first TEXT NOT NULL,
    name_last TEXT NOT NULL,
    hand TEXT,
    dob DATE,
    ioc TEXT,
    height INTEGER,
    wikidata_id TEXT
);

CREATE TABLE tournaments (
    tourney_id TEXT PRIMARY KEY,
    tourney_name TEXT NOT NULL,
    surface TEXT CHECK(surface IN ('Hard', 'Clay', 'Grass', 'Carpet')),
    draw_size INTEGER,
    tourney_level TEXT,
    tourney_date DATE
);

CREATE TABLE matches(
    tourney_id TEXT NOT NULL REFERENCES tournaments(tourney_id),
    match_num INTEGER NOT NULL,
    winner_id INTEGER NOT NULL REFERENCES players(player_id),
    winner_seed INTEGER,
    winner_entry TEXT,
    winner_age REAL,
    loser_id INTEGER NOT NULL REFERENCES players(player_id),
    loser_seed INTEGER,
    loser_entry TEXT,
    loser_age REAL,
    score TEXT,
    best_of INTEGER,
    round TEXT,
    minutes INTEGER,
    winner_rank INTEGER,
    winner_rank_points INTEGER,
    loser_rank INTEGER,
    loser_rank_points INTEGER,
    PRIMARY KEY (tourney_id, match_num)
);

CREATE TABLE match_stats (
    tourney_id TEXT NOT NULL,
    match_num INTEGER NOT NULL,
    w_ace INTEGER,
    w_df INTEGER,
    w_svpt INTEGER,
    w_1stIn INTEGER,
    w_1stWon INTEGER,
    w_2ndWon INTEGER,
    w_SvGms INTEGER,
    w_bpSaved INTEGER,
    w_bpFaced INTEGER,
    l_ace INTEGER,
    l_df INTEGER,
    l_svpt INTEGER,
    l_1stIn INTEGER,
    l_1stWon INTEGER,
    l_2ndWon INTEGER,
    l_SvGms INTEGER,
    l_bpSaved INTEGER,
    l_bpFaced INTEGER,
    FOREIGN KEY (tourney_id, match_num) REFERENCES matches(tourney_id, match_num),
    PRIMARY KEY (tourney_id, match_num)
);