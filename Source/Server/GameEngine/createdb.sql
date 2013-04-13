-- vi: spell spl=en
--
-- timestamps are in the format YYYY-MM-DD HH:MM:SS.SS
--
--

create table games
(
    game_id integer primary key asc, --  test_id in the other tables.
    name    text not null
);

create table players
(
    id       integer primary key asc, -- Concat of X and Y pos 
    game_id  integer,
    name     text not null
);

create table planets
(
    id       integer primary key asc, -- Concat of X and Y pos 
    game_id  integer,
    name     text not null,
    -- No two planets in the same game share the exact
    -- same x and y coordinate.
    x        integer not null,
    y        integer not null
);


