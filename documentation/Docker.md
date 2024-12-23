# Docker Usage for End Users

1. Open Docker Desktop to start the docker daemon
2. Navigate to projects root directory
3. Optionally login to the DoIt Container Registry with `docker login`
4. Run `docker compose -p sudoku up` to build images, install dependencies, and run the container
5. Access Sudoku by navigating to `localhost:3000` in your web browser
6. Press `C-c` to exit docker

# Docker Usage for Developers

1. Either use the end-users' one-liner and make sure to include `--build` or build individually with:
   - `docker compose -p sudoku build`
   - `docker compose up` or `docker compose up -d`to run detached
2. Access:
   - Frontend: localhost:3000
   - Backend: localhost:8000/sudoku
3. `docker compose ps` to list project containers or `docker ps -a` to list all containers
4. `docker compose stop` to stop containers if detached
5. `docker compose down` to stop and delete containers

## Using CLI with Docker:

MySQL: `docker exec -it <db_id_or_name> sh`

```sh
mysql -u user -p
> Enter password: password
```

Django: `docker exec -it <backend_id_or_name> sh`

```sh
django-admin ...
python manage.py makemigrations
```

Node: `docker exec -it <frontend_id_or_name> sh`

```sh
node ...
```

## Want to Delete All Images/Containers/Networks/Volumes?

To remove sudoku related: `docker compose down --rmi all --volumes`

To remove everything: `docker stop $(docker ps -aq) && docker system prune -af --volumes`

## Deployment

When ready for deployment switch to npm ci for faster builds!

```
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
        --mount=type=cache,target=/root/.npm \
            npm ci --omit=dev
```
