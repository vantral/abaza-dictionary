# Инструкция

## GoldenDict

Нужно скачать определённую версию GoldenDict, которая поддерживает скрипты (можно жить и без скриптов, но со скриптами веселее).

Точно рабочие версии:

- [Windows](https://sourceforge.net/projects/goldendict/files/early%20access%20builds/)
- [Mac](https://sourceforge.net/projects/goldendict/files/early%20access%20builds/MacOS/)

## Словарь

Собственно словарь хранится в этом репозитории в подпапке `dic`. Нужно положить эту подпапку, как и подпапку `scripts`, но о ней позднее -- в какую-то удобную папку, откуда GoldenDict будет доставать словарь.

Чтобы добавить словарь в приложение GoldenDict, нужно нажать следующие кнопки `Правка > Словари` (или просто `F3`). Дальше нужно нажать на кнопку добавить и указать путь к папке `dic`, которую уже положили в удобное для вас место. И поставьте галочку на `рекурсивно`.

После этого у вас в списке должен появиться Абазинско-русский словарь.

## Скрипты

Есть два скрипта.

- `full_text.py` allows for searching within dictionary entries (full text search). To enable it, one should begin the input with `|`.
![](https://github.com/Even-UD/Golden-Even/blob/main/full_text.png?raw=true)

- `substring.py` allows one to search lemmas by substring, not just the begining of the word. Do not forget to press `Enter` to enable this type of search!

Чтобы активировать скрипты, нужно открыть GoldenDict, перейти по `Правка > Словари > Программы` (если у вас нет вкладки `Программы`, то у вас не та версия GoldenDict). Дальше нужно добавить две строчки (тип HTML) в поле `Коммандная строка`.

`/path/to/your/python` -- обычно это просто `python` или `python3`.

ВАЖНО: надо заменить бэкслэши Windows на обычные слэши в пути.

- `/path/to/your/python "path/to/scripts/full_text.py" %GDWORD% "path/to/dic/abaza-russian.dsl"`
- `/path/to/your/python "path/to/scripts/substring.py" %GDWORD% "path/to/dic/dictionary.dsl"`

Если что-то не получается, то идёте ко мне (антону).
