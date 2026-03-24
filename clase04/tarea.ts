class Figura{
    public constructor (public color:string){
        
    }
}
class Rectangulo extends Figura{
    public constructor (public base:number,public atura:number,color:string){
        super (color);
    }
    public getArea():number{ 
        return this.base*this.atura
    }
    public getBase(): number {
        return this.base;
    }
    public getAltura():number{
        return this.atura
    }
    public setBase(nuevaBase:number){
        this.base = nuevaBase
    }
    public setAltura(nuevaAltura:number){
        this.atura = nuevaAltura
    }
}
const rectagulo1=new Rectangulo(10,2,'azul');
console.log(rectagulo1)
console.log(rectagulo1.getArea())
rectagulo1.setAltura(30)
console.log(rectagulo1)
console.log(rectagulo1.getArea())