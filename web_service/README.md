### set alias in ~/.bashrc or ~/.zshrc
```bash
alias dc='docker-compose'
alias rpm='dc exec web python manage.py'
alias rpmsh='dc exec web python manage.py shell_plus
```

### Run
```bash
cd web
. ./build.sh
dc up -d
```