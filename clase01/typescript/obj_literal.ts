/*
let persona :{nombre:string; apellido:string}= {
    nombre:"Juan",
    apellido:"Perez"
}
console.log(persona);
*/
interface Persona{
    nombre:string,
    apellido:string,
    direccion:Direccion
};
interface Direccion{
    ciudad:string,
    calle:string,
    numero:number
};

//let, var , const
let direccion={
    ciudad:"La Paz",
    calle:"calle falsa",
    numero:123
};

let persona :Persona ={
    nombre: "Juan",
    apellido:"Perez",
    direccion:direccion
    
}
//const copiaPersona = persona; //copia el puntero del area de memoria
//const copiaPersona = {...persona}; //copia el objeto en su totalidad de manera superficial, ineficiente si se tiene una estructura interna
const copiaPersona = structuredClone(persona);

persona.nombre="Luis";
persona.direccion.ciudad="Tarija"
//console.log(`Nombre: ${persona.apellido} ${persona.nombre}\nDireccion: ${persona.direccion.calle} ${persona.direccion.numero} en ${persona.direccion.ciudad}`);
//console.log(`Nombre: ${copiaPersona.apellido} ${copiaPersona.nombre}\nDireccion: ${persona.direccion.calle} de ${copiaPersona.direccion.ciudad}`);
console.log(persona);
console.log(copiaPersona);