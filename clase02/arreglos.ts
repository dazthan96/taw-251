export{}
//sintaxis con corchetes
let v:number[] = [1,2,3,4,5]
//console.log(v)
v.push(6)
v.push(7)
//console.log(v)
/**for(const x of v){
    console.log(x)
};**/
let v1:Array<number> = [1,2,3,4,5]
v1.push(6)
//console.table(v1)
//lista mixta

let mixto:(string | number)[] =[1, "hola"]
//console.table(mixto)

interface Persona{
    id: number;
    nombre: string;
}

let personas:Persona[]=[
    {
        id:1,
        nombre:"pedro"
    },
    {
        id:2,
        nombre:"rosmery"
    }
]
//console.table(personas)
let p1 = personas
//let p1 = structuredClone(personas)
p1[0] = {
    id:0,
    nombre:"ABC"
};
//console.table(personas)
//console.table(p1)
//tuple 
let personav2:[string, number];
personav2 = ['juan', 123]
//console.table(personav2)
let r:[codigo:number, mensaje:string] = [100, "ok"]
//console.table(r);

function fun1():[number, string]{
    return [1,"juan"]
}
const [id, nombre] = fun1();
//console.log(id, nombre)
//tarea se tiene un arreglo de persona(nombre, edad).se desea imprimir los objetos que tengan una edad entre 20 y 30
interface Personav3{
    nombre:string;
    edad:number
}
let personasv3:Personav3[]=[
    {
        nombre:"rosmery",
        edad:26
    },
    {
        nombre:"anabel",
        edad:31
    },
    {
        nombre:"maya",
        edad:18
    }
]
for (const personav3 of personasv3) {
    if(personav3.edad >=20 && personav3.edad<=30){
        console.log(personav3)
    }
}