import { Injectable } from '@nestjs/common';
import { CreateProductDto } from './dto/create-product.dto';
import { UpdateProductDto } from './dto/update-product.dto';
import { Repository } from 'typeorm';
import { InjectRepository } from '@nestjs/typeorm';
import { Product } from './entities/product.entity';
import { NotFoundError } from 'rxjs';

export interface Producto{
  id:number;
  nombre:string;
  precio:number
}

//@InjectRepository(Product)
@Injectable()
export class ProductService {
  
  constructor(
    @InjectRepository(Product)
    private readonly productoRepository:Repository<Product>
  ){}
  /*private productos: Producto[]=[
    { id:1, nombre:"producto 1", precio:10 },
    { id:2, nombre:"producto 2", precio:20 },
    { id:3, nombre:"producto 3", precio:30 }
  ];*/
  async create(createProductDto: CreateProductDto) {
    const producto = this.productoRepository.create(createProductDto);
    return await this.productoRepository.save(producto);
  }

  async findAll():Promise<Product[]> {
    return await this.productoRepository.find();
  }

  async findOne(id: number){
    const p1 = this.productoRepository.findOneBy({id:id});
    if(!p1){
      throw new NotFoundError('producto no encontrado')
    }else{
      return p1;
    }
    
  }

  async update(id: number, updateProductDto: UpdateProductDto) {
    
    return `This action updates a #${id} product`;
  }

  remove(id: number) {
    return `This action removes a #${id} product`;
  }
}
