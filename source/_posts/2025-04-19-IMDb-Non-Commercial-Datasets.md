---
title: IMDb Non-Commercial Datasets
category: unknown
tags: []
comments: true
date: 2025-04-19 21:05:39
---

# IMDb Non-Commercial Datasets

from: https://developer.imdb.com/non-commercial-datasets/

## Official doc

Those are the 7 tables. 

1.  **title.akas.tsv.gz**

    *   titleId (string) - a tconst, an alphanumeric unique identifier of the title
    *   ordering (integer) – a number to uniquely identify rows for a given titleId
    *   title (string) – the localized title. Those have more than 150 titles: 
        *   tt0088814
        *   tt0168366
        *   tt0407304
        *   tt1077274
        *   tt15837206
        *   tt0099785
        *   tt2872750
    *   region (string) - the region for this version of the title
    *   language (string) - the language of the title. Eg 5M of jp/JP, 4.8M of hi/IN, fr/FR, es/ES, 51K of cmn/CN etc. 
    *   types (array) - Enumerated set of attributes for this alternative title. One or more of the following: 
        *   "alternative"
        *   "dvd"
        *   "festival"
        *   "tv"
        *   "video"
        *   "working"
        *   "original"
        *   "imdbDisplay"
    *   attributes (array) - Additional terms to describe this alternative title, not enumerated. One or none of the following: 
        *   transliterated title
        *   alternative spelling
        *   new title
        *   literal English title
        *   complete title
        *   literal title
        *   short title
        *   series title
    *   isOriginalTitle (boolean) – 0: not original title; 1: original title. Of the 52M titles, 12M are original title, and 6M have 0 or 1 variant title.

1.  **title.basics.tsv.gz**

    *   tconst (string) - alphanumeric unique identifier of the title
    *   titleType (string) – the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)
    *   primaryTitle (string) – the more popular title / the title used by the filmmakers on promotional materials at the point of release
    *   originalTitle (string) - original title, in the original language
    *   isAdult (boolean) - 0: non-adult title; 1: adult title
    *   startYear (YYYY) – represents the release year of a title. In the case of TV Series, it is the series start year
    *   endYear (YYYY) – TV Series end year. '\\N' for all other title types
    *   runtimeMinutes – primary runtime of the title, in minutes
    *   genres (string array) – includes up to three genres associated with the title

1.  **title.crew.tsv.gz**

    *   tconst (string) - alphanumeric unique identifier of the title
    *   directors (array of nconsts) - director(s) of the given title
    *   writers (array of nconsts) – writer(s) of the given title

1.  **title.episode.tsv.gz**

    *   tconst (string) - alphanumeric identifier of episode
    *   parentTconst (string) - alphanumeric identifier of the parent TV Series
    *   seasonNumber (integer) – season number the episode belongs to
    *   episodeNumber (integer) – episode number of the tconst in the TV series

1.  **title.principals.tsv.gz**

    *   tconst (string) - alphanumeric unique identifier of the title
    *   ordering (integer) – a number to uniquely identify rows for a given titleId
    *   nconst (string) - alphanumeric unique identifier of the name/person
    *   category (string) - the category of job that person was in
    *   job (string) - the specific job title if applicable, else '\\N'
    *   characters (string) - the name of the character played if applicable, else '\\N'

1.  **title.ratings.tsv.gz**

    *   tconst (string) - alphanumeric unique identifier of the title
    *   averageRating – weighted average of all the individual user ratings
    *   numVotes - number of votes the title has received

1.  **name.basics.tsv.gz**

    *   nconst (string) - alphanumeric unique identifier of the name/person
    *   primaryName (string)– name by which the person is most often credited
    *   birthYear – in YYYY format
    *   deathYear – in YYYY format if applicable, else '\\N'
    *   primaryProfession (array of strings)– the top-3 professions of the person
    *   knownForTitles (array of tconsts) – titles the person is known for

## Insert Order

1.  **`title_basics`**
    *   **Reason:** This is the root table. Many other tables depend on it via foreign keys (`tconst`). It must be populated first.
    *   **Dependencies:** None (it's the foundation).
    *   **Tables that depend on it:**
        *   `title_akas`
        *   `title_crew`
        *   `title_episode`
        *   `title_principals`
        *   `title_ratings`

2.  **`name_basics`**
    *   **Reason:**  `title_principals` depends on it via the `nconst` foreign key.
    *   **Dependencies:** None (except the implicit dependency that `tconst` in `known_for_titles` should exist in `title_basics`, but this is not a strict foreign key constraint).
    *   **Tables that depend on it:**
        *   `title_principals`

3.  **`title_crew`**
    *   **Reason:** Depends on `title_basics` via the `tconst` foreign key.
    *   **Dependencies:**
        *   `title_basics`
    *   **Tables that depend on it:** None

4.  **`title_episode`**
    *   **Reason:** Depends on `title_basics` via both `tconst` and `parent_tconst` foreign keys.
    *   **Dependencies:**
        *   `title_basics`
    *   **Tables that depend on it:** None

5.  **`title_ratings`**
    *   **Reason:** Depends on `title_basics` via the `tconst` foreign key.
    *   **Dependencies:**
        *   `title_basics`
    *   **Tables that depend on it:** None

6.  **`title_principals`**
    *   **Reason:** Depends on both `title_basics` (via `tconst`) and `name_basics` (via `nconst`).
    *   **Dependencies:**
        *   `title_basics`
        *   `name_basics`
    *   **Tables that depend on it:** None

7.  **`title_akas`**
    *   **Reason:** Depends on `title_basics` via the `title_id` foreign key.
    *   **Dependencies:**
        *   `title_basics`
    *   **Tables that depend on it:** None

## Detailed Instructions

```
gzip -d name.basics.tsv.gz \
    && gzip -d title.akas.tsv.gz \
    && gzip -d title.basics.tsv.gz \
    && gzip -d title.crew.tsv.gz \
    && gzip -d title.episode.tsv.gz \
    && gzip -d title.principals.tsv.gz \
    && gzip -d title.ratings.tsv.gz
```

replace \N characters with empty values in order to import them as NULLs, according to a blog post from [metis](https://www.metisdata.io/blog/skyrocket-your-database-performance-with-metis-playing-with-imdb-data)

```
sed 's/\\N//g' name.basics.tsv > name.basics.tsv2 \
	&& sed 's/\\N//g' title.akas.tsv > title.akas.tsv2 \
	&& sed 's/\\N//g' title.basics.tsv > title.basics.tsv2 \
	&& sed 's/\\N//g' title.crew.tsv > title.crew.tsv2 \
	&& sed 's/\\N//g' title.episode.tsv > title.episode.tsv2 \
	&& sed 's/\\N//g' title.principals.tsv > title.principals.tsv2 \
	&& sed 's/\\N//g' title.ratings.tsv > title.ratings.tsv2 \
	&& rm *.tsv
```

In psql: 

```
psql -d postgres
CREATE SCHEMA IF NOT EXISTS imdb;
\i /path/to/create_table.sql -- Run the script
\dn imdb  -- List schemas, check if imdb exists
\dt imdb.* -- List all tables in the imdb schema
```

Last, copy data:

```
\copy imdb.title_basics FROM '/database/title.basics.tsv2' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;
\copy imdb.name_basics FROM '/database/name.basics.tsv2' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;
\copy imdb.title_crew FROM '/database/title.crew.tsv2' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;
\copy imdb.title_episode FROM '/database/title.episode.tsv2' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;
\copy imdb.title_ratings FROM '/database/title.ratings.tsv2' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;
\copy imdb.title_principals FROM '/database/title.principals.tsv2' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;
\copy imdb.title_akas FROM '/database/title.akas.tsv2' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;
\q  -- Quit psql
```

# SQL

```
-- Schema: imdb

-- Table: title_akas
-- Represents alternative titles for a movie/show.
CREATE TABLE imdb.title_akas (
    title_id VARCHAR(20) NOT NULL, -- tconst of the title in title_basics
    ordering SMALLINT NOT NULL, -- Number to uniquely identify rows for each titleId
    title TEXT NOT NULL, -- The localized title
    region VARCHAR(10), -- The region for this version of the title
    language VARCHAR(10), -- The language for this version of the title
    types TEXT[], -- Array of types for this version of the title
    attributes TEXT[], -- Array of attributes for this version of the title
    is_original_title BOOLEAN, -- Whether this is the original title
    PRIMARY KEY (title_id, ordering)
);

-- Table: title_basics
-- Represents basic information about a movie/show.
CREATE TABLE imdb.title_basics (
    tconst VARCHAR(20) PRIMARY KEY, -- Alphanumeric unique identifier of the title
    title_type VARCHAR(50) NOT NULL, -- The type/format of the title (e.g., movie, short, tvEpisode)
    primary_title TEXT NOT NULL, -- The more popular title
    original_title TEXT NOT NULL, -- Original title, in the original language
    is_adult BOOLEAN, -- Whether the title is adult-oriented
    start_year INTEGER, -- Year the title was released
    end_year INTEGER, -- Year the title ended (for TV series)
    runtime_minutes INTEGER, -- Length of the title in minutes
    genres TEXT[], -- Array of genres for the title
    CHECK (start_year > 1800),
    CHECK (end_year >= start_year)
);

-- Table: title_crew
-- Represents the crew (directors and writers) for a movie/show.
CREATE TABLE imdb.title_crew (
    tconst VARCHAR(20) PRIMARY KEY, -- tconst of the title in title_basics
    directors VARCHAR(20)[], -- Array of nconsts of directors
    writers VARCHAR(20)[] -- Array of nconsts of writers
);

-- Table: title_episode
-- Represents information about a TV episode.
CREATE TABLE imdb.title_episode (
    tconst VARCHAR(20) PRIMARY KEY, -- tconst of the episode in title_basics
    parent_tconst VARCHAR(20), -- tconst of the parent series in title_basics
    season_number INTEGER, -- Season number of the episode
    episode_number INTEGER, -- Episode number within the season
    CHECK (season_number > 0),
    CHECK (episode_number > 0)
);

-- Table: title_principals
-- Represents the principal cast and crew for a movie/show.
CREATE TABLE imdb.title_principals (
    tconst VARCHAR(20) NOT NULL, -- tconst of the title in title_basics
    ordering SMALLINT NOT NULL, -- Number to uniquely identify rows for each tconst
    nconst VARCHAR(20), -- nconst of the person in name_basics
    category VARCHAR(50) NOT NULL, -- The role of the person (e.g., actor, director)
    job TEXT, -- The specific job of the person
    characters TEXT, -- The characters played by the person
    PRIMARY KEY (tconst, ordering)
);

-- Table: title_ratings
-- Represents the ratings for a movie/show.
CREATE TABLE imdb.title_ratings (
    tconst VARCHAR(20) PRIMARY KEY, -- tconst of the title in title_basics
    average_rating DECIMAL(3,1), -- Average rating of the title
    num_votes INTEGER NOT NULL, -- Number of votes for the title
    CHECK (num_votes >= 0),
    CHECK (
        (num_votes > 0 AND average_rating >= 0 AND average_rating <= 10) OR
        (num_votes = 0 AND average_rating IS NULL)
    )
);

-- Table: name_basics
-- Represents basic information about a person.
CREATE TABLE imdb.name_basics (
    nconst VARCHAR(20) PRIMARY KEY, -- Alphanumeric unique identifier of the name
    primary_name TEXT NOT NULL, -- Name by which the person is most commonly known
    birth_year INTEGER, -- Year the person was born
    death_year INTEGER, -- Year the person died
    primary_profession TEXT[], -- Array of professions for the person
    known_for_titles VARCHAR(20)[], -- Array of tconsts of titles the person is known for
    CHECK (birth_year > 1800),
    CHECK (death_year >= birth_year)
);

-- Foreign Key Constraints

-- title_akas
ALTER TABLE imdb.title_akas
ADD CONSTRAINT fk_title_akas_title_basics
FOREIGN KEY (title_id)
REFERENCES imdb.title_basics(tconst)
ON DELETE CASCADE
ON UPDATE RESTRICT;

-- title_crew
ALTER TABLE imdb.title_crew
ADD CONSTRAINT fk_title_crew_title_basics
FOREIGN KEY (tconst)
REFERENCES imdb.title_basics(tconst)
ON DELETE CASCADE
ON UPDATE RESTRICT;

-- title_episode
ALTER TABLE imdb.title_episode
ADD CONSTRAINT fk_title_episode_title_basics
FOREIGN KEY (tconst)
REFERENCES imdb.title_basics(tconst)
ON DELETE CASCADE
ON UPDATE RESTRICT;

ALTER TABLE imdb.title_episode
ADD CONSTRAINT fk_title_episode_parent_title_basics
FOREIGN KEY (parent_tconst)
REFERENCES imdb.title_basics(tconst)
ON DELETE SET NULL
ON UPDATE RESTRICT;

-- title_principals
ALTER TABLE imdb.title_principals
ADD CONSTRAINT fk_title_principals_title_basics
FOREIGN KEY (tconst)
REFERENCES imdb.title_basics(tconst)
ON DELETE CASCADE
ON UPDATE RESTRICT;

ALTER TABLE imdb.title_principals
ADD CONSTRAINT fk_title_principals_name_basics
FOREIGN KEY (nconst)
REFERENCES imdb.name_basics(nconst)
ON DELETE CASCADE
ON UPDATE RESTRICT;

-- title_ratings
ALTER TABLE imdb.title_ratings
ADD CONSTRAINT fk_title_ratings_title_basics
FOREIGN KEY (tconst)
REFERENCES imdb.title_basics(tconst)
ON DELETE CASCADE
ON UPDATE RESTRICT;

-- Indexes
CREATE INDEX idx_title_akas_region ON imdb.title_akas (region);
CREATE INDEX idx_title_akas_language ON imdb.title_akas (language);
CREATE INDEX idx_title_basics_title_type ON imdb.title_basics (title_type);
CREATE INDEX idx_title_basics_start_year ON imdb.title_basics (start_year);
CREATE INDEX idx_title_basics_genres ON imdb.title_basics USING GIN (genres);
CREATE INDEX idx_title_episode_parent_tconst ON imdb.title_episode (parent_tconst);
CREATE INDEX idx_title_principals_nconst ON imdb.title_principals (nconst);
CREATE INDEX idx_name_basics_primary_profession ON imdb.name_basics USING GIN (primary_profession);
```