---
title: IMDb Non-Commercial Datasets
category: database
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

If use docker on Mac:
```
docker volume create imdb_data
docker run -d \
	--name imdb-postgres \
	-e POSTGRES_USER=imdb \
	-e POSTGRES_PASSWORD=1234 \
	-e POSTGRES_DB=imdb_db \
	-p 5432:5432 \
	-v imdb_data:/var/lib/postgresql/data \
	-v /Users/mac/Downloads/imdb:/data/imdb \
	postgres:latest
docker ps
docker exec -it imdb-postgres psql -U imdb -d imdb_db
docker exec -i  imdb-postgres psql -U imdb -d imdb_db < /Users/mac/Downloads/imdb/scripts/create_table.sql
```

Now you've created Postgres with username/password `imdb/1234`, and db name `imdb_db`

### Import data dump into Postgres

Seems like there's slight issue with the genres of title_basics, thus need to convert the comma-separated list in the last field to a PostgreSQL array format

Run this: 

```
awk -F'\t' -v OFS='\t' '{if ($9 != "") $9 = "{"$9"}"; print}' title.basics.tsv2 > title.basics.tsv3
docker exec -i imdb-postgres psql -U imdb -d imdb_db -c "\copy imdb.title_basics FROM '/data/imdb/title.basics.tsv3' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;"
```

Great it works! 

![IMDb-Non-Commercial-Datasets](/images/IMDb-Non-Commercial-Datasets.png)

### 2nd Table

```
awk -F'\t' -v OFS='\t' '{if ($5 != "") $5 = "{"$5"}"; if ($6 != "") $6 = "{"$6"}"; print}' name.basics.tsv2 > name.basics.tsv3
docker exec -i imdb-postgres psql -U imdb -d imdb_db -c "\copy imdb.name_basics FROM '/data/imdb/name.basics.tsv3' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;"
```

Small problem with this [person](https://www.imdb.com/name/nm10019610/), thus line 938151 is empty, we need to remove it.

```
sed -n '938151p' name.basics.tsv3 # Read this line
sed '938151d' name.basics.tsv3 > name.basics.tsv4
docker exec -i imdb-postgres psql -U imdb -d imdb_db -c "\copy imdb.name_basics FROM '/data/imdb/name.basics.tsv4' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;"
```

After this I somehow I need to run 

```
insert into imdb.name_basics values ('nm17199025', 'Kay Masten')
insert into imdb.name_basics values ('nm0203940', 'Robert Davies')
```

to avoid a fk_title_principals_name_basics error (in later stage).

Alternatively: `ALTER TABLE imdb.name_basics ALTER COLUMN primary_name DROP NOT NULL;` does the trick well! 

### 3nd to 7th Tables

```
docker exec -i imdb-postgres psql -U imdb -d imdb_db -c "\copy imdb.title_crew FROM '/data/imdb/title.crew.tsv2' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;"

docker exec -i imdb-postgres psql -U imdb -d imdb_db -c "\copy imdb.title_episode FROM '/data/imdb/title.episode.tsv2' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;"

docker exec -i imdb-postgres psql -U imdb -d imdb_db -c "\copy imdb.title_ratings FROM '/data/imdb/title.ratings.tsv2' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;"

docker exec -i imdb-postgres psql -U imdb -d imdb_db -c "\copy imdb.title_principals FROM '/data/imdb/title.principals.tsv2' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;"

TODO

docker exec -i imdb-postgres psql -U imdb -d imdb_db -c "\copy imdb.title_akas FROM '/data/imdb/title.akas.tsv2' DELIMITER E'\t' QUOTE E'\b' CSV HEADER;"
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
    directors text, -- Array of nconsts of directors
    writers text -- Array of nconsts of writers
);

-- Table: title_episode
-- Represents information about a TV episode.
CREATE TABLE imdb.title_episode (
    tconst VARCHAR(20) PRIMARY KEY, -- tconst of the episode in title_basics
    parent_tconst VARCHAR(20), -- tconst of the parent series in title_basics
    season_number INTEGER, -- Season number of the episode
    episode_number INTEGER, -- Episode number within the season
    CHECK (season_number > 0)
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

## Updated schema (live data)

Type changes:

    directors VARCHAR(20)[]
    writers VARCHAR(20)[]

Remove checks:

    CHECK (season_number > 0),
    CHECK (episode_number > 0)
    CHECK (birth_year > 1800),
    CHECK (death_year >= birth_year)

Remove some unavailable titles from `principals` table.

```
DELETE FROM imdb.title_principals
WHERE tconst IN (
    'tt36455508', 'tt0229782', 'tt1464025', 'tt36587729', 'tt36490446',
    'tt30062722', 'tt30063520', 'tt32868697', 'tt36415652', 'tt10719918',
    'tt36042551', 'tt6118406', 'tt8141116', 'tt27726906', 'tt36491536',
    'tt11024622', 'tt33567817', 'tt36590614', 'tt7205998', 'tt13478388',
    'tt14512626', 'tt2277124', 'tt26455860', 'tt32909558', 'tt34221354',
    'tt36270736', 'tt36590638', 'tt8264988', 'tt21451682', 'tt26455938',
    'tt26455946', 'tt26455958', 'tt5801700', 'tt7019426', 'tt7019888',
    'tt18987786', 'tt36480536', 'tt36480540', 'tt36480705', 'tt36480911',
    'tt36481055', 'tt36481157', 'tt36481176', 'tt36481178', 'tt36481184',
    'tt36586613'
);
```

Updated Table as of Apr 20th, 2025: 

```
-- imdb.name_basics definition

-- Drop table

-- DROP TABLE imdb.name_basics;

CREATE TABLE imdb.name_basics (
	nconst varchar(20) NOT NULL,
	primary_name text NOT NULL,
	birth_year int4 NULL,
	death_year int4 NULL,
	primary_profession _text NULL,
	known_for_titles _varchar NULL,
	CONSTRAINT name_basics_pkey PRIMARY KEY (nconst)
);
CREATE INDEX idx_name_basics_primary_profession ON imdb.name_basics USING gin (primary_profession);


-- imdb.title_basics definition

-- Drop table

-- DROP TABLE imdb.title_basics;

CREATE TABLE imdb.title_basics (
	tconst varchar(20) NOT NULL,
	title_type varchar(50) NOT NULL,
	primary_title text NOT NULL,
	original_title text NOT NULL,
	is_adult bool NULL,
	start_year int4 NULL,
	end_year int4 NULL,
	runtime_minutes int4 NULL,
	genres _text NULL,
	CONSTRAINT title_basics_check CHECK ((end_year >= start_year)),
	CONSTRAINT title_basics_pkey PRIMARY KEY (tconst),
	CONSTRAINT title_basics_start_year_check CHECK ((start_year > 1800))
);
CREATE INDEX idx_title_basics_genres ON imdb.title_basics USING gin (genres);
CREATE INDEX idx_title_basics_start_year ON imdb.title_basics USING btree (start_year);
CREATE INDEX idx_title_basics_title_type ON imdb.title_basics USING btree (title_type);


-- imdb.title_akas definition

-- Drop table

-- DROP TABLE imdb.title_akas;

CREATE TABLE imdb.title_akas (
	title_id varchar(20) NOT NULL,
	"ordering" int2 NOT NULL,
	title text NOT NULL,
	region varchar(10) NULL,
	"language" varchar(10) NULL,
	"types" varchar(10) NULL,
	"attributes" text NULL,
	is_original_title bool NULL,
	CONSTRAINT title_akas_pkey PRIMARY KEY (title_id, ordering),
	CONSTRAINT title_akas_title_basics_fk FOREIGN KEY (title_id) REFERENCES imdb.title_basics(tconst) ON DELETE CASCADE ON UPDATE RESTRICT
);
CREATE INDEX idx_title_akas_language ON imdb.title_akas USING btree (language);
CREATE INDEX idx_title_akas_region ON imdb.title_akas USING btree (region);


-- imdb.title_crew definition

-- Drop table

-- DROP TABLE imdb.title_crew;

CREATE TABLE imdb.title_crew (
	tconst varchar(20) NOT NULL,
	directors text NULL,
	writers text NULL,
	CONSTRAINT title_crew_pkey PRIMARY KEY (tconst),
	CONSTRAINT fk_title_crew_title_basics FOREIGN KEY (tconst) REFERENCES imdb.title_basics(tconst) ON DELETE CASCADE ON UPDATE RESTRICT
);


-- imdb.title_episode definition

-- Drop table

-- DROP TABLE imdb.title_episode;

CREATE TABLE imdb.title_episode (
	tconst varchar(20) NOT NULL,
	parent_tconst varchar(20) NULL,
	season_number int4 NULL,
	episode_number int4 NULL,
	CONSTRAINT title_episode_pkey PRIMARY KEY (tconst),
	CONSTRAINT title_episode_season_number_check CHECK ((season_number > 0)),
	CONSTRAINT fk_title_episode_parent_title_basics FOREIGN KEY (parent_tconst) REFERENCES imdb.title_basics(tconst) ON DELETE SET NULL ON UPDATE RESTRICT,
	CONSTRAINT fk_title_episode_title_basics FOREIGN KEY (tconst) REFERENCES imdb.title_basics(tconst) ON DELETE CASCADE ON UPDATE RESTRICT
);
CREATE INDEX idx_title_episode_parent_tconst ON imdb.title_episode USING btree (parent_tconst);


-- imdb.title_principals definition

-- Drop table

-- DROP TABLE imdb.title_principals;

CREATE TABLE imdb.title_principals (
	tconst varchar(20) NOT NULL,
	"ordering" int2 NOT NULL,
	nconst varchar(20) NULL,
	category varchar(50) NOT NULL,
	job text NULL,
	"characters" text NULL,
	CONSTRAINT title_principals_pkey PRIMARY KEY (tconst, ordering),
	CONSTRAINT title_principals_title_basics_fk FOREIGN KEY (tconst) REFERENCES imdb.title_basics(tconst) ON DELETE CASCADE ON UPDATE RESTRICT
);
CREATE INDEX title_principals_nconst_idx ON imdb.title_principals USING btree (nconst);


-- imdb.title_ratings definition

-- Drop table

-- DROP TABLE imdb.title_ratings;

CREATE TABLE imdb.title_ratings (
	tconst varchar(20) NOT NULL,
	average_rating numeric(3, 1) NULL,
	num_votes int4 NOT NULL,
	CONSTRAINT title_ratings_check CHECK ((((num_votes > 0) AND (average_rating >= (0)::numeric) AND (average_rating <= (10)::numeric)) OR ((num_votes = 0) AND (average_rating IS NULL)))),
	CONSTRAINT title_ratings_num_votes_check CHECK ((num_votes >= 0)),
	CONSTRAINT title_ratings_pkey PRIMARY KEY (tconst),
	CONSTRAINT fk_title_ratings_title_basics FOREIGN KEY (tconst) REFERENCES imdb.title_basics(tconst) ON DELETE CASCADE ON UPDATE RESTRICT
);
```

Below 3291 people are present in title_principals, but missing from name_basics.

That's why I have to drop the `fk_title_principals_name_basics` constraint. 

```
SELECT tp.nconst , COUNT(*) as count
FROM imdb.title_principals tp
LEFT JOIN imdb.name_basics nb ON tp.nconst = nb.nconst
WHERE nb.nconst IS NULL
GROUP BY tp.nconst 
ORDER BY count DESC;
```

Also, need to convert text format of directors, writers column of `title_crew` to list format. 
