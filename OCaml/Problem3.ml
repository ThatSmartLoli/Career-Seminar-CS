type 'a priority_queue =
  | Empty
  | Node of int * 'a * 'a priority_queue * 'a priority_queue;;

  let rec is_Empty = function
  | Empty -> true
  | _ -> false;;

let rec merge firstPQ secondPQ =
    match firstPQ, secondPQ with
    | Empty, priorityQueue | priorityQueue, Empty -> priorityQueue
    | Node (priorityOne, valuesOne, left1, right1), Node(priorityTwo, valuesTwo, left2, right2) ->
      if priorityOne <= priorityTwo then
        Node (priorityOne, valuesOne, right1, merge left1 secondPQ)
      else
        Node (priorityTwo, valuesTwo, right2, merge firstPQ left2);;

let insert x priority priorityQueue =
  let insert_Node = Node (priority, x, Empty, Empty) in
  merge priorityQueue insert_Node;;

  let remove = function
  | Empty -> None
  | Node (priority, values, left, right) ->
    Some (values, merge left right);;

let pq = Empty;;
is_Empty pq;;
let pq = insert "task1" 5 pq;;
let pq = insert "task2" 3 pq;;
let pq = insert "task3" 7 pq;;
let pq = insert "task3" 1 pq;;
is_Empty pq;;
let pq, removed = match remove pq with
  | None -> pq, None
  | Some (value, newPQ) -> newPQ, Some value;;

removed;;