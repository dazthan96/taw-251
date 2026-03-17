//Desestructuracion de Objeto
export{}
interface Persona{
    id?:number;
    nombre:string;
    apellido:string;
    edad:number
}
const persona:Persona = {
    id:1,
    nombre:"rosmery",
    apellido:"larico",
    edad:29
}
//tradicional
/*const nombre = persona.nombre;
const apellido = persona.apellido;
const edad = persona.edad;
console.log(nombre, apellido, edad);*/
//nuevo
//const {nombre:a, apellido:b, edad:c} = persona;
//console.log(a,b,c)

const miFuncion = ():Persona =>{
    return {
        nombre:"anabel",
        apellido:"paredes",
        edad:28
    }
} 
const {nombre:user}=miFuncion()
console.log(user)

const miFuncion2 = (p:Persona):Persona =>{
    const {nombre} = p;
    return {
        nombre,
        apellido:"paredes",
        edad:28
    }
} 
const {nombre,apellido}=miFuncion2(persona)
console.log(nombre,apellido)
const miFuncion3 = (p:Persona)=>{
    const {nombre} = p;
    return {
        id:2,
        usuario:{
            nombre,
            apellido:"paredes",
            edad:28
        }
    }
}
const {id:indice, usuario:users} = miFuncion3(persona);
console.log(indice, users.nombre);
//console.table([id, usuario])
//const {id:indice2, usuario:nombre} = miFuncion3(persona);
//console.log(indice2, nombre)
