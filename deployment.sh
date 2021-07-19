#!/usr/bin/env bash

USAGE="Usage: bash deployment.sh [production] [up|down|build|logs|rm]"

environment=$1
cmd=$2

if [[ ${cmd} == "up" ]]; then
	cmd="up -d"
fi
if [[ ${cmd} == "rm" ]]; then
	cmd="rm -f"
fi
if [[ ${cmd} == "logs" ]]; then
	cmd="logs -f"
fi
if [[ ${cmd} == "build" ]]; then
	cmd="up -d --build"
fi

## Production
if [[ "$environment" == "production" ]] && [[ "$2" == "down" ]]; then
	docker-compose -f docker-compose.production.yml ${cmd}
elif [[ "$environment" == "production" ]] && [[ "$2" == "up" ]]; then
	docker-compose -f docker-compose.production.yml ${cmd}
elif [[ "$environment" == "production" ]] && [[ "$2" == "build" ]]; then
	docker-compose -f docker-compose.production.yml ${cmd}
elif [[ "$environment" == "production" ]] && [[ "$2" == "logs" ]]; then
	docker-compose -f docker-compose.production.yml ${cmd}
elif [[ "$environment" == "production" ]] && [[ "$2" == "rm" ]]; then
  docker ps -q --filter "name=carp-client-api-flask" | grep -q . && docker stop carp-client-api-flask || "CARP Client API could not be stopped." && docker rm -f carp-client-api-flask > /dev/null 2>&1 && echo 'removed container' || echo 'nothing to remove' && docker rmi -f carp-client-api-flask || echo "There is no carp-client-api-flask container to purge." && docker volume rm -f carp-client-api-flask || echo "The carp-client-api-flask does not exist in volume."
else
	echo "${USAGE}"
fi