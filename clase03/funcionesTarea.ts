interface Persona {
    nombre:string;
    edad:number
}
// funcion anonima, flecha y flecha abrevidad
const objeto1 = function():Persona{
    return {
        nombre:"Rosmery",
        edad:26
    }
};
console.log(objeto1())

const objeto2 = (): Persona =>{
    return {
        nombre:"Pedro",
        edad:46
    };
}
console.log(objeto2())
const objeto3 = (x:string, y:number):Persona =>({nombre:x, edad:y});
console.log(objeto3("nana",30))
// Ejemplo de función flecha con múltiples parámetros y lógica
const procesarDatos = (datos:Array<number>, factor:number) => {
    const filtrados = datos.filter(item => item > 10);
    return filtrados.map(item => item * factor);
};
console.log(procesarDatos([1,14,15,80],2));