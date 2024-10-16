type general_tree =
         | Empty
         | Node of int list * general_tree list;;

let rec height = function
         | Empty -> 0
         | Node (_, childern) -> 1 + List.fold_left ( fun acc child -> max acc (height child)) 0 childern;;         


let tree = Node ( [2;5], [ Node ([1], [Empty;Empty]);
         Node ([3;4], [Empty;Node ([6], [Empty; Empty]);Empty]);]);;

let rec inorder tree =
    match tree with
          | Empty -> []
          | Node(value, child) -> List.fold_left(fun acc child -> acc @ inorder child) [] child @ value;; 

let rec preorder tree =
    match tree with
          | Empty -> []
          |  Node(value, child) -> value @ List.fold_left(fun acc child -> acc @ preorder child) [] child;; 

let rec postorder tree =
    match tree with
          | Empty -> []
          | Node(value, child) -> List.fold_left(fun acc child -> acc @ postorder child) [] child @ value;; 

let rec insert target value tree =
    match tree with
          | Empty -> Empty
          | Node(v, child) ->
            if v = target then
              Node(v, Node(value, []) :: child)
            else
              Node(v, List.map (insert target value) child);;

height tree;;
preorder tree;;
inorder tree;;
postorder tree;;
let inserttree = insert [6] [7] tree;;
height inserttree;;
preorder inserttree;;
inorder inserttree;;
postorder inserttree;;