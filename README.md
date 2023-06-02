# Purrs

Purrs fetches the RSS feeds from various sources, sorts and categorizes them, and makes them viewable in a web ui.

## Building the Docker image

To build the Docker image, run:s.

```bash
docker build -t purrs .
```

## TODO (roughly in order)

1. ingest data from > 1 subreddit
1. setup db schema
1. save data into sqlite
1. basic deduplicate data
1. web ui display text items
1. web ui like/dislike buttons write to db
1. web ui shows more item types
1. make MD representations of items
1. embed all test representations and save to db
1. model training?
1. expand this todo list



<!-- non-mvp material commented out -->
```mermaid
flowchart TD
    subgraph database
        item
        source
        %%user
        vector
        item_score
        model
    end
    source --> item

    subgraph scrape
        rss_reader
        url_specific_parser
        diff_check
    end
    source --urls--> rss_reader
    rss_reader --raw feed--> url_specific_parser
    url_specific_parser --raw rss items--> diff_check

    subgraph embed
        text_representations
        embeddings_engine
    end
    item --new and unread items--> text_representations
    text_representations --markdown--> embeddings_engine
    embeddings_engine --vectors--> vector

    subgraph training
        training_data
        ml_model
    end
    vector --> training_data
    item --seen items--> training_data
    training_data --> ml_model
    ml_model --> model

    subgraph scoring
        scoring_model
    end
    model --best performing recently--> scoring_model
    item --never/stale scored--> scoring_model
    scoring_model --> item_score

    subgraph ui
        %%admin
        config
        main
    end
    source <--> config
    %%admin --> user
```


```mermaid
erDiagram
    item {
        item_id id
        source_id id
        title string
        body string
        raw_xml string
        ingest_date date
        seen bool "true, false"
        opened bool "true, false and null"
        liked bool "true, false and null"
    }

    item_source {
        item_source_id id
        name string
        url string
        source type
        auth string
    }

    item_score {
        item_id id
        model_id id
        score float
        confidence float
    }

    model {
        model_id id
        train_date date
        tp int
        fp int
        tn int
        fn int
        weights string
    }

    vector_source {
        vector_source_id id
    }

    vector {
        item_id id
        source id
    }

    users {
        id id
        name string
        hashed_password string
        write bool
        admin bool
    }

    item ||--|| item_source : from
    vector ||--|| vector_source : from
    item ||--|| vector : describes
    item ||--|| item_score : ranks
    item_score ||--|| model : produces
```