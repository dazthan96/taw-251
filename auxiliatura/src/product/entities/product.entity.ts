import { Column, Entity, PrimaryColumn, PrimaryGeneratedColumn } from "typeorm";

@Entity()
export class Product {
    @PrimaryGeneratedColumn()
    id:number;
    @Column({nullable:false,type:"varchar",length:50})
    nombre:string;
    @Column({nullable:false,type:"numeric",precision:10,scale:2})
    costo:number
}
