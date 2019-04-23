# Andrea & Charles Bronfman Philanthropies

This repo is for Vipul Naik's Donations List Website: https://github.com/vipulnaik/donations

Relevant issue: https://github.com/vipulnaik/donations/issues/95

## Instructions for running the scripts

Download the data into CSV:

```bash
./scrape.py > data.csv
```

Use the CSV to generate the SQL file:

```bash
./proc.py data.csv > out.sql
```

## License

CC0 for scripts and readme.
