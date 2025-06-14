# Проєкт: Алгоритми для графів (NetworkX)

## Завдання 1: Граф — транспортна мережа

Модель: метро міста  
Станції: вузли  
Маршрути: ребра

Візуалізовано граф.  
Проведено аналіз:
- Вершин: 9
- Ребер: 10
- Ступені: центральна станція — найбільш з'єднана.

## Завдання 2: DFS vs BFS

Пошук шляху між `University` → `Airport`:
- **DFS**: обирає шлях в глибину (не обов'язково найкоротший)
- **BFS**: завжди повертає найкоротший шлях

 Результат:
```
DFS path: ['University', 'North', 'Central', 'South', 'Stadium', 'Airport']
BFS path: ['University', 'North', 'Central', 'East', 'Airport']
```


## Завдання 3: Алгоритм Дейкстри

У граф додано ваги ребер.  
Знайдено найкоротші шляхи між усіма парами вершин.
 
Для прикладу:
```
Найкоротші шляхи з Central:
до North: ['Central', 'North']
до South: ['Central', 'South']
до East: ['Central', 'East']
до West: ['Central', 'West']
до Museum: ['Central', 'West', 'Museum']
до Stadium: ['Central', 'South', 'Stadium']
до University: ['Central', 'West', 'Museum', 'University']
до Airport: ['Central', 'South', 'Stadium', 'Airport']
```