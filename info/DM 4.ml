(* Exercice 30 : RAS *)

(* Exercice 31 *)

(* Fonction A *)

let rec ppp2 n exposant = (*prend un exposant en argument or la fonction est censée prendre uniquement un entier en argument*)
  if n <= (2. ** exposant) (*utilise des flottants or l'exercice n'implique l'utilisation que d'entiers, il y a une erreur de type*)
  then (2. ** exposant) 
  else 
    (
      if n > (2. ** exposant) (*test inutile, n est toujours soit inférieur ou égal, soit strictement supérieur à 2. ** exposant*)
      then ppp2 n (exposant +. 1.) (*reprend n en argument sans le modifier, on peut faire une sous-fonction ne prenant que l'argument exposant*)
      else 0. (*cas inutile car le test est inutile*)
    );;
(*on notera aussi le triple calcul de 2.**exposant qui pourrait être éliminé si on passait directement la valeur en argument et qu'on appelait la fonction avec 2*.exposant au lieu de exposant +. 1.*)


(* Exercice 32 *)

(* Fonction B *)

let leeloo l =
  let r = ref l in
  r := List.rev !r;
  while List.length !r > 5 do
    r := List.tl !r done;
  List.hd !r;;
(*utilisation des fonctions issues de List au lieu de l'opérateur natif :: et utilisation d'une boucle au lieu d'une fonction récursive, 
la liste n'a pas été traitée en tant que liste mais en tant que tableau*) 

(* Exercice 33 *)

(* Fonction C *)

let rec coupe l = 
let b = ref [] in
let c = ref [] in
for i=0 to (List.length l)-1 do
if i mod 2 = 0 then b := (!b)@[List.nth l i] else c := (!c)@[List.nth l i]done; 
(!b,!c);;
(*la fonction est déclarée en tant que fonction récurisve or elle ne fait pas de récursion, elle utilise une boucle et traite la liste comme un tableau*)

(* Fonction D *)

let coupe liste=
let rec aux k x liste =
match liste with
|[]->[]
|a::q-> if x mod 2 =k then a::(aux k (x+1) q) else aux k (x+1) q in
(aux 0 0 liste, aux 1 0 liste);;
(*parcours deux fois la liste alors que cela pourrait être fait en un seul passage en stockant les deux listes dans les arguments de la fonction récusive*)
(* Fonction E *)

let coupe l = 
  let m = [] and n = [] in (*déclaration de m et n en tant que variables de coupe*)
  let rec coupage l m n = match l with (*déclaration de m et n en tant qu'arguments de coupage, fonctionne mais peu esthétique car se base sur le recouvrement par les variables locales*)
    |[] -> (m, n)
    |[a] -> if List.length m = List.length n then (m@[a], n) else (m, n@[a]) (*inutile, pris en compte par le cas d'après*)
    |hd::tl -> if List.length m = List.length n then 
          coupage tl (m@[hd]) n else coupage tl m (n@[hd])
  in coupage l m n;;

(* Fonction F *)
 
let rec coupe l = match l with
	| [] -> failwith "oups"
	| [e] -> (l, [])
	| t::q -> ([t]@(fst (coupe (List.tl q))), [List.hd q]@(snd (coupe (List.tl q)))) (*List.tl q correspond à l à laquelle on a enlevé t et le dernier élémént de q.
  le nombre d'éléments de la liste en argument diminue donc par 2 à chaque appel, ce qui fait que la liste devient vide sans atteindre le cas de base si elle contient initialement un nombre pair d'éléments*)

(* Exercice 34 *)

(* Fonction G *)

let colle l1 l2 = 
    let rec collage l l1 l2 = match l1 with (*recouvrement par variables locales*)
    | [] -> l
    | a::s -> match l2 with (*test inutile au vu de l'énoncé*)
        | [] -> l
        | b::t -> collage (l@[a]@[b]) s t (*complexité linéaire de l'opérateur @, peut être réduite en écrivant a::b::collage s t et en renvoyant une liste vide dans le cas de base, 
                                          cette syntaxe retire la nécessité d'un troisième argument pour garder en mémoire la liste à renvoyer*)
    in collage [] l1 l2;;

(* Exercice 35 : RAS *)

(* Exercice 36 *)

(* Fonction H *)

let rec sommesi list pred =
  match list with
  |[] -> 0
  |a::reste -> if pred a = true then a+sommesi reste pred else 0+sommesi reste pred;;

(* Exercice 37 *)

(* Fonction I *)

let majopred l p =
	if l=[] then false else
	let y = List.length l in
	let rec majop l p n = match l with
	|a::q -> if p a then majop q p (n+1) else majop q p n
	|[] -> if n >= ((y+1)/2) then true else false
in majop l p 0;;

(* Fonction J *)

let majopred l pred =
let moitié = if (List.length l) mod 2 = 1 then 
(List.length l)/2 + 1 else (List.length l)/2 in
print_int moitié;
let n =
let rec combien l pred = match l with
| []->0
| a::q -> if pred a then 1 + combien q pred 
else combien q pred;
in combien l pred;
in n>=moitié;;

(* Fonction K *)

let majopred liste predicat = 
let rec aux liste predicat = match liste with
|[]-> 0
|a::q -> if predicat a then 1 + aux q predicat else aux q predicat
in let taille = List.length liste 
in if aux liste predicat > taille / 2 then true else false;;

(* Fonction L *)

let rec majopred l f =
	let rec aux l f [|i; n|] =
		match l with
			|[] -> [|i; n|]
			|a::q -> if f a then [|i + 1; n + 1|] else [|i; n + 1|]
			in float_of_int (aux l f [|0;  0|]).(0) >= float_of_int (aux l f [|0; 0|]).(1) /. 2.;;

(* Exercice 18 *)

(* Fonction M *)

let rec lexico l1 l2 = match l1,l2 with
| [],[] -> true
| a::q,b::r -> if a<b then lexico q r else false;;

(* Fonction N *)

let rec lexico l1 l2 = match l1 with 
	|[] -> if l2=[] then failwith ("liste identiques") else true
	|a::q -> match l2 with
	|[] -> false
	|b::r -> if a<b then true else if a>b then false else lexico q r;;

(* Exercice 19 *)

(* Fonction O *)

let rec aplatir l1 l2 = match l1 with
  | [] -> l2
  | a::q -> a::(aplatir q l2) ;; 

(* Fonction P *)

let aplatir l1 =
    let nlist = ref [] in
    let tab = Array.of_list l1 in
    
    for i = 0 to ((Array.length tab)-1) do 
    
    nlist:= !nlist @ tab.(i)
    done ; nlist ;;

(* Fonction Q *)

let aplatir l1 =
  let rec ap l1 l2= match l1 with
    |a::q-> ap q (l2@[a])
    |[]->l2
  in
  let rec app l1 lresult= match l1 with
    |a::q -> app q (lresult@ap a [] )
    |[] -> lresult
  in
  app l1 [];;