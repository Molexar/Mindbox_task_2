## Testing Task of Junior Data Engineer
### Developed by Nikita Potasev

### Stack:
- FastApi
- Postgresql
- SQLAlchemy
- pytest

### ENV File:
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

### Deploying:
```
docker-compose up --build
```

### API Docs
```
127.0.0.1/docs
```

### Testing
```
docker exec mindbox_2_app_1 pytest
```

### Links to get lists of objects:
```127.0.0.1/products```
<br>
```127.0.0.1/categories```
<br>
```127.0.0.1/products-categories```