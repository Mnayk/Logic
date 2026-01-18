from telethon.sync import TelegramClient # pip install telethon
from telethon import functions, types
import asyncio
import time  # Для пауз, чтобы не нагружать API

# Ваши API credentials (получите на my.telegram.org)
api_id = None  # Замените на свой
api_hash = 'hash'  # Замените на свой
phone = '+number'  # Ваш номер телефона в формате +1234567890
# Все равно первый раз в консоли потребуется залогиниться с паролем и кодом доступа, потом не нужно

# Вместо ID можно использовать username группы (без @, например 'mygroup' для t.me/mygroup)
group_username = None  # Замените на username группы, или None если используете ID
# Проще всего group ID узнать через web.telegram.org - отрицательный номер будет в URL группы
group_id = None  # Или укажите ID напрямую, например -1001234567890

# Количество сообщений для проверки (чтобы не сканировать всю историю)
message_limit = 10  # Маленькое число для теста, увеличьте позже


async def main():
    async with TelegramClient('session', api_id, api_hash) as client:
        # Авторизация (если сессия новая, введите код из Telegram)
        if not await client.is_user_authorized():
            await client.send_code_request(phone)
            code = input('Введите код из Telegram: ')
            await client.sign_in(phone, code)

        # Получаем entity группы
        if group_username:
            group = await client.get_entity(group_username)
            group_id_actual = group.id
            print(f"Найден чат по username '{group_username}': Название: {group.title}, ID: {group_id_actual}")
        else:
            group = await client.get_entity(group_id)
            group_id_actual = group_id
            print(f"Чат по ID {group_id}: Название: {group.title}")

        # Подтверждение: правильный ли чат?
        confirm = input("Это правильный чат? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Отмена. Измените group_username или group_id и попробуйте снова.")
            return

        # Получаем последние сообщения
        messages = await client.get_messages(group, limit=message_limit)
        my_id = (await client.get_me()).id  # Ваш user ID

        # Фильтруем только ваши сообщения
        my_messages = [msg for msg in messages if msg.from_id and msg.from_id.user_id == my_id]

        if not my_messages:
            print("Не найдено ваших сообщений в последних {message_limit}.")
            return

        # Показываем и удаляем ОДНО сообщение для теста
        first_msg = my_messages[0]
        print("\nПервое ваше сообщение для теста:")
        print(f"ID: {first_msg.id}, Дата: {first_msg.date}, Текст: {first_msg.text or '[Без текста, возможно медиа]'}")

        confirm_delete_one = input("Удалить это сообщение для всех? (y/n): ").strip().lower()
        if confirm_delete_one == 'y':
            try:
                await client.delete_messages(group, first_msg.id, revoke=True)  # revoke=True удаляет для всех
                print(f"Удалено сообщение ID: {first_msg.id}")
            except Exception as e:
                print(f"Ошибка при удалении: {e}")
        else:
            print("Удаление одного сообщения отменено.")

        # Теперь спрашиваем про все остальные
        if len(my_messages) > 1:
            print(f"\nНайдено ещё {len(my_messages) - 1} ваших сообщений.")
            confirm_all = input("Удалить все остальные ваши сообщения? (y/n): ").strip().lower()
            if confirm_all == 'y':
                deleted_count = 0
                for msg in my_messages[1:]:  # Пропускаем первое, если оно уже обработано
                    try:
                        await client.delete_messages(group, msg.id, revoke=True)
                        deleted_count += 1
                        print(f"Удалено сообщение ID: {msg.id}; deleted_count: {deleted_count} из {len(my_messages) - 1}")
                        time.sleep(0.7)  # Пауза 1 сек, чтобы избежать лимитов API
                    except Exception as e:
                        print(f"Ошибка при удалении ID {msg.id}: {e}")
                print(f"Всего удалено: {deleted_count} сообщений (плюс первое, если удалено).")
            else:
                print("Удаление остальных отменено.")
        else:
            print("Больше сообщений не найдено.")

# Запуск
asyncio.run(main())
