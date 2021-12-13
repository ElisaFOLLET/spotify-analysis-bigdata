#!/usr/bin/env bash

terraform init

cd ../../..
cp -r anaconda3/envs/pipeline/Lib/site-packages/spotipy PycharmProjects/pipeline/lambda_payloads/
cp -r anaconda3/envs/pipeline/Lib/site-packages/requests PycharmProjects/pipeline/lambda_payloads/

cp PycharmProjects/pipeline/track_features_top_playlist.py PycharmProjects/pipeline/lambda_payloads/
cp PycharmProjects/pipeline/config/playlists.py PycharmProjects/pipeline/lambda_payloads/config/
cp PycharmProjects/pipeline/connection/refresh.py PycharmProjects/pipeline/lambda_payloads/connection/
cp PycharmProjects/pipeline/connection/secrets.py PycharmProjects/pipeline/lambda_payloads/connection/


