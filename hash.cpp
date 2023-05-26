// Program to implement Hashing with Linear Probing
#include<iostream>
#define SIZE 13
using namespace std;
 
class hashTable{
   
    private:
        int table[SIZE], elementCount;
   
    public:
   
        // initialize hash Table
        hashTable(){
            for(int i=0; i < SIZE; i++){
                table[i] = 0;
            }
            elementCount = 0;
        }
       
        // method that checks if the hash table is full or not
        bool isFull(){
            if(elementCount == SIZE){
                return true;
            }else{
                return false;
            }
        }
       
       
        // method that returns position for a given element
        int hashFunction(int element){
            return element % SIZE;
        }  
       
        // method that inserts element inside the hash table
        void insert(int element){
            int position;
            // checking if the table is full
            if(this->isFull()){
                cout<<"\nHash Table Full";
                return;
            }  
           
            bool isStored = false;
           
            position = this->hashFunction(element);
               
            // checking if the position is empty
            if(table[position] == 0){
                table[position] = element;
                cout<<"\nElement " <<element<<" at position " <<position;
                isStored = true;
                elementCount += 1;
            }  
           
            // collision occured hence we do linear probing
            else{
                cout<<"\nCollision has occured for element " <<element<<" at position " <<position<<" finding new Position.";
                while(table[position] != 0){
                    position += 1;
                    if(position >= SIZE){
                        position = 0;
                    }
                }  
                table[position] = element;
                isStored = true;
                elementCount += 1;
            }  
            return;
        }  
 
        // method that searches for an element in the table
        // returns position of element if found
        // else returns false
        int search(int element){
            bool found = false;
           
            int position = this->hashFunction(element);
           
            if(table[position] == element){
                found = true;
                return position;
            }  
           
            // if element is not found at position returned hash function
            // then first we search element from position+1 to end
            // if not found then we search element from position-1 to 0
            else{
                int temp = position - 1;
                // check if the element is stored between position+1 to size
                while(position < SIZE){
                    if(table[position] != element){
                        position += 1;
                    }else{ 
                        return position;
                    }  
                }
               
                // now checking if the element is stored between position-1 to 0
                position = temp;
                while(position >= 0){  
                    if(table[position] != element){
                        position -= 1;
                    }else{ 
                        return position;
                    }
                }
            }  
            if(!found){
                cout<<"\nElement not found";
                return -1;
            }
        }  
       
       
        // method to remove an element from the table      
        void remove(int element){
            int position = this->search(element);
            if(position != -1){
                table[position] = 0;
                cout<<"\nElement " <<element<<" is Deleted";
                this->elementCount -= 1;
            }else{
                cout<<"\nElement is not present in the Hash Table";
            }
            return;
        }  
       
        // method to display the hash table
        void display(){
            for (int i = 0; i < SIZE; i++){
                cout<<"\n"<<i<<" = "<<table[i];
            }  
            cout<<"\nThe number of element is the Table are : " <<this->elementCount;
        }  
};     
 
int main(){
    // main function
    hashTable table1;
 
    // storing elements in table
    table1.insert(12);
    table1.insert(26);
    table1.insert(31);
    table1.insert(17);
    table1.insert(90);
    table1.insert(28);
    table1.insert(88);
    table1.insert(40);
    table1.insert(77);      // element that causes collision at position 0
 
    // displaying the Table
    table1.display();
    cout<<"\n";
 
    // printing position of elements
    cout<<"\nThe position of element 31 is : " <<table1.search(31);
    cout<<"\nThe position of element 28 is : " <<table1.search(28);
    cout<<"\nThe position of element 90 is : " <<table1.search(90);
    cout<<"\nThe position of element 77 is : " <<table1.search(77);
    cout<<"\nThe position of element 1 is : " <<table1.search(1);
 
    cout<<"\n";
 
    table1.remove(90);
    table1.remove(12);
 
    table1.display();
}