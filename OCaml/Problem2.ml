type 'a polymorphic_stack =
    | Empty
    | Stack of 'a  * 'a polymorphic_stack;;

let stack = Stack(1,Stack(2, Empty));;
let eStack = Stack(1,Empty);;

let rec is_Empty = function
    | Empty -> true
    | _ -> false;;

let rec push a b = Stack(a,b);;
let rec pop = function
    | Empty -> failwith "Stack Empty"
    | Stack (x,xs) -> (x,xs);; 


is_Empty stack;;
let stack1 = push 3 stack;;
let (popped,stack2) = pop stack1;;
let stack3 = push 4 stack2;;

let eStack1 = push 3 eStack;;
let (popped,eStack2) = pop eStack1;;
let (poppedAgain,eStack3) = pop eStack2;;
is_Empty eStack3;;
