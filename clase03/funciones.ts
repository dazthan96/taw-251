export{}
/*
//funciones
function saludar(x:string):string{
    return `Hola ${x}`;
}

console.log(saludar("pedro"));
*/
//funcion anonima
/*
const saludar = function(x:string):string{
    return `hola ${x}`
};
console.log(saludar("pedro"));
const a = saludar;
console.log(a("pedro"));*/
//funcion flecha
/*
const saludar = (x:string): string =>{
    return `hola ${x}`;
}
console.log(saludar("pedro"));
const a = saludar;
console.log(a("pedro"));*/
//funcion flecha abreviada

/*const saludar = (x:string): string =>`hola ${x}`;
console.log(saludar("pedro"));
const a = saludar;
console.log(a("pedro"));*/
//funcion tradicional
interface Persona{
    nombre:string;
    edad:number
}
function obtObjeto():Persona{
    return {
        nombre:"juan",
        edad:20
    };
}
console.log(obtObjeto())