DROP TABLE IF EXISTS pedroacastagnola_coderhouse.api_tmdb_pelis_terror;

CREATE TABLE pedroacastagnola_coderhouse.api_tmdb_pelis_terror(

    id integer,
    title VARCHAR(250),
    original_language VARCHAR(10),
    overview VARCHAR(1000),
    release_date DATE,
    vote_average FLOAT,
    vote_count FLOAT,
    insert_date TIMESTAMP,
    primary key(id,release_date)
);