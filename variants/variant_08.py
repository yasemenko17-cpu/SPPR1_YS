import os
import time

VARIANT = 23

def spawn_orphans(path: str, n: int, label: str) -> int:
    """
    Створює дитину, яка породжує n онуків і завершується. 
    Онуки чекають на зміну PPID (осиротіння) і дописують у файл повідомлення.
    """
    pid = os.fork()
    
    if pid == 0:
        # Код дитини (середнього процесу)
        for k in range(1, n + 1):
            g_pid = os.fork()
            if g_pid == 0:
                # Код онука
                original_ppid = os.getppid()
                start_time = time.time()
                
                # Чекаємо, доки батько зміниться (стане 1), з запасом часу
                while os.getppid() == original_ppid:
                    if time.time() - start_time > 10.0:
                        break
                    time.sleep(0.005)
                
                # Якщо n > 0, записуємо результат у файл
                if n > 0:
                    try:
                        with open(path, 'a', encoding='utf-8') as f:
                            f.write(f"{label} {k}: усиновлено\n")
                    except Exception:
                        pass
                
                os._exit(0)
        
        # Дитина завершується одразу, не чекаючи на онуків
        os._exit(0)
    else:
        # Батьківський процес чекає лише на свою пряму дитину
        _, status = os.waitpid(pid, 0)
        
        # Даємо невелику паузу, щоб усі онуки встигли завершити записи у файл
        if n > 0:
            time.sleep(0.15)
            
        return os.waitstatus_to_exitcode(status)