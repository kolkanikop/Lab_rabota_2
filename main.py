import requests

# Замените на ваш токен и username
TOKEN = "your_github_token"
USERNAME = "your_username"

headers = {"Authorization": f"token {TOKEN}"}

def get_user_stats():
    # Получаем информацию о пользователе
    user_url = f"https://api.github.com/users/{USERNAME}"
    user_data = requests.get(user_url, headers=headers).json()
    
    # Получаем список репозиториев (упрощённо, берём первые 100)
    repos_url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
    repos = requests.get(repos_url, headers=headers).json()
    
    total_stars = sum(r['stargazers_count'] for r in repos)
    total_forks = sum(r['forks_count'] for r in repos)
    
    print(f"Пользователь: {USERNAME}")
    print(f"Публичные репозитории: {user_data.get('public_repos')}")
    print(f"Подписчики: {user_data.get('followers')}")
    print(f"Всего звёзд: {total_stars}")
    print(f"Всего форков: {total_forks}")

if __name__ == "__main__":
    get_user_stats()
