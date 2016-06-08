if [[ -z $DB_PORT_6379_TCP_ADDR ]];
then
    echo DB host variable not set. Exiting
    exit 1
else
    echo "Writing to config.json"
    echo -e "{\n\t\"REDIS_HOST\": \"$DB_PORT_6379_TCP_ADDR\"\n}" > config.json

    cat config.json
fi
