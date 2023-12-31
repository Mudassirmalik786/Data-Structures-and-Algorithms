#include <iostream>
using namespace std;

class Node{
    public:
    int data;
    bool color; //1 for red, 0 for black
    Node* parent;
    Node* left;
    Node* right;
    Node(int data){
        this->data=data;
        this->parent=NULL;
        this->left=NULL;
        this->right=NULL;
    }
    ~Node(){
        delete parent;
        delete left;
        delete right;
        this->parent=NULL;
        this->left=NULL;
        this->right=NULL;
    }
};
class BST{
    private:
    Node* root=NULL;
    public:
    BST(){
    }
    BST(int arr[],int size){
        for (int i=0;i<size;i++){
            Insert(arr[i]);
        }
    }
    ~BST(){
        root=NULL;
    }
    bool isEmpty(){
        if (root==NULL){
            return true;
        }
        else{
            return false;
        }
    }
    Node* getTree(){
        return root;
    }
    void Insert(int data){
        Node *z =new Node(data);
        Node *y=NULL; //Trailing pointer
        Node *x=root; //Parent of BST
        while(x!=NULL){
            y=x;
            if(z->data < x->data){
                x=x->left;
            }
            else{
                x=x->right;
            }
        }
        z->parent=y; //Make the parent
        if(y==NULL){
            root=z;
        }
        else if(z->data < y->data){
            y->left=z;
        }
        else{
        y->right=z;
        }
    }
    Node* findNode(int data){
        Node* x=root;
        while(x!=NULL && x->data!=data){
            if(data<x->data){
                x=x->left;
            }
            else{
                x=x->right;
            }
        }
        return x;
    }
    bool deleteNode(int x){
        Node* z=findNode(x);
        if(z==NULL){
            return false;
        }
        else{
            if(z->left==NULL){
                transplant(z,z->right);
            }
            else if(z->right==NULL){
                transplant(z,z->left);
            }
            else{
                Node* y=treeMinimum(z->right);
                if(y->parent!=z){
                    transplant(y,y->right);
                    y->right=z->right;
                    y->right->parent=y;
                }
                transplant(z,y);
                y->left=z->left;
                y->left->parent=y;
            }
            delete z;
            return true;
        }
    }
    void transplant(Node* u,Node* v){
        if(u->parent==NULL){
            root=v;
        }
        else if(u==u->parent->left){
            u->parent->left=v;
        }
        else{
            u->parent->right=v;
        }
        if(v!=NULL){
            v->parent=u->parent;
        }
    }
    Node* treeMinimum(Node* x){
        while(x->left!=NULL){
            x=x->left;
        }
        return x;
    }

    void inOrderTraversal(Node *p){
        if(p!=NULL){
            inOrderTraversal(p->left);
            cout<<p->data<<" ";
            inOrderTraversal(p->right);
        }
        cout<<endl;
    }
    void preOrderTraversal(Node *p){
        if(p!=NULL){
            cout<<p->data<<" ";
            preOrderTraversal(p->left);
            preOrderTraversal(p->right);
        }
        cout<<endl;
    }
    void postOrderTraversal(Node *p){
        if(p!=NULL){
            postOrderTraversal(p->left);
            postOrderTraversal(p->right);
            cout<<p->data<<" ";
        }
        cout<<endl;
    }
    int numberOfNodes(Node *p){
        if(p==NULL){
            return 0;
        }
        else{
            return numberOfNodes(p->left)+numberOfNodes(p->right)+1;
        }
    }
    int height(Node* T){
        if(T==NULL){
            return 0;
        }
        else{
            int lheight=height(T->left);
            int rheight=height(T->right);
            if(lheight>rheight){
                return lheight+1;
            }
            else{
                return rheight+1;
            }
        }
    }
    bool isBST(Node *T){
        if(T==NULL){
            return true;
        }
        else{
            if(T->left!=NULL && T->left->data>T->data){
                return false;
            }
            if(T->right!=NULL && T->right->data<T->data){
                return false;
            }
            if(!isBST(T->left) || !isBST(T->right)){
                return false;
            }
            return true;
        }
    }
    void leafNodes(Node *T){
        if(T!=NULL){
            if(T->left==NULL && T->right==NULL){
                cout<<T->data<<" ";
            }
            leafNodes(T->left);
            leafNodes(T->right);
        }
    }
    void visualizeTree(Node *T,int space){
        if(T==NULL){
            return;
        }
        space+=10;
        visualizeTree(T->right,space);
        cout<<endl;
        for(int i=10;i<space;i++){
            cout<<" ";
        }
        cout<<T->data<<endl;
        visualizeTree(T->left,space);
    }  
};
class RbTree:BST{
    private:
    public:
    Node* root=NULL;
    RbTree(){
    }
    RbTree(int arr[],int size){
        for (int i=0;i<size;i++){
           Insert(arr[i]); //it will be changed
        }
    }
    ~RbTree(){
        root=NULL;
    }
    void printInorder(Node *p){
        if(p!=NULL){
            printInorder(p->left);
            cout<<p->data<<" ";
            printInorder(p->right);
        }
        cout<<endl;
    }
    void visualizeTree(Node* T,int space){
        Node* node=T;
        if(node==NULL){
            return;
        }
        space+=10;
        visualizeTree(node->left,space);
        cout<<endl;
        for(int i=10;i<space;i++){
            cout<<" ";
        }
        cout<<node->data<<" C:"<<node->color<<endl;
        visualizeTree(node->right,space);
    }
    
    void Insert(int data){  
        Node *z =new Node(data);
        Node *y=NULL; //Trailing pointer
        Node *x=root; //Parent of BST
        while(x!=NULL){//these are trailing to find the exact location for inseration
            y=x;
            if(z->data < x->data){
                x=x->left;
            }
            else{
                x=x->right;
            }
        }
        z->parent=y; //Make the parent
        if(y==NULL){//run only first time
            root=z;
        }
        else if(z->data < y->data){
            y->left=z;
        }
        else{
        y->right=z;
        }
        // z->left=NULL;
        // z->right=NULL;
        z->color=true; //make red color
        RBInsertFixup(z);
    }

    void RBInsertFixup(Node* z){
        Node *y=NULL;
        while(z->parent!=NULL &&z->parent->color==true){
            if(z->parent==z->parent->parent->left){
                y=z->parent->parent->right;
                if(y!=NULL &&y->color==true){
                    z->parent->color=false;           //case1
                    y->color=false;                   //case1
                    z->parent->parent->color=true;   //case1
                    z=z->parent->parent;            //case1
                }
                else {
                    if (z==z->parent->right){
                    z=z->parent;                    //case2
                    leftRotate(z);                  //case2
                    }                 
                    z->parent->color=false;           //case3
                    z->parent->parent->color=true;   //case3
                    rigthRotate(z->parent->parent); //case3
                }            
            }
            else{
                y=z->parent->parent->left;
                if(y!=NULL &&y->color==true){
                    z->parent->color=false;           //case1
                    y->color=false;                   //case1
                    z->parent->parent->color=true;   //case1
                    z=z->parent->parent;            //case1
                }
                else{
                    if (z==z->parent->left){
                    z=z->parent;                    //case2
                    rigthRotate(z);                  //case2
                    }                  
                    z->parent->color=false;           //case3
                    z->parent->parent->color=true;   //case3
                    leftRotate(z->parent->parent); //case3
                }  
            }
        }
        root->color=false;
    }
    void leftRotate(Node*x){
        Node *y=x->right;
        x->right=y->left;
        if(y->left!=NULL){
            y->left->parent=x;
        }
        y->parent=x->parent;
        if(x->parent==NULL){
            root=y;
        }
        else if(x==x->parent->left){
            x->parent->left=y;
        }
        else{
            x->parent->right=y;
        }
        y->left=x;
        x->parent=y;
    }
    void rigthRotate(Node*x){
        Node *y=x->left;
        x->left=y->right;
        if(y->right!=NULL){
            y->right->parent=x;
        }
        y->parent=x->parent;
        if(x->parent==NULL){
            root=y;
        }
        else if(x==x->parent->right){
            x->parent->right=y;
        }
        else{
            x->parent->left=y;
        }
        y->right=x;
        x->parent=y;
    }
    Node* search(int data){
        Node* x=root;
        while(x!=NULL && x->data!=data){
            if(data<x->data){
                x=x->left;
            }
            else{
                x=x->right;
            }
        }
        return x;
    }
    void RBTransplant(Node* u,Node* v){
        if(u->parent==NULL){
            root=v;
        }
        else if(u==u->parent->left){
            u->parent->left=v;
        }
        else{
            u->parent->right=v;
        }
        if(v!=NULL){
            v->parent=u->parent;
        }
    }
    Node* TreeMinimum(Node* x){
        while(x->left==NULL){
            x=x->left;
        }
        return x;
    }
    void RBDelete(int data){
        Node* z=search(data);
        Node* y=z;
        Node* x=NULL;
        bool yOriginalColor=y->color;
        if(z->left==NULL){
            x=z->right;
            RBTransplant(z,z->right);
        }
        else if(z->right==NULL){
            x=z->left;
            RBTransplant(z,z->left);
        }
        else{
            y=TreeMinimum(z->right);
            yOriginalColor=y->color;
            x=y->right;
            if(y->parent==z){
                x->parent=y;
            }
            else{
                RBTransplant(y,y->right);
                y->right=z->right;
                y->right->parent=y;
            }
            RBTransplant(z,y);
            y->left=z->left;
            y->left->parent=y;
            y->color=z->color;
        }
        if(yOriginalColor==false){
            RBDeleteFixup(x);
        }
    }
    void RBDeleteFixup(Node* x){
        Node* w=NULL;
        while(x!=root && x->color==false){
            if(x==x->parent->left){
                w=x->parent->right;
                if(w->color==true){
                    w->color=false;                 //case1
                    x->parent->color=true;          //case1
                    leftRotate(x->parent);          //case1
                    w=x->parent->right;             //case1
                }
                if(w->left->color==false && w->right->color==false){
                    w->color=true;                  //case2
                    x=x->parent;                    //case2
                }
                else{
                    if(w->right->color==false){
                        w->left->color=false;       //case3
                        w->color=true;              //case3
                        rigthRotate(w);             //case3
                        w=x->parent->right;         //case3
                    }
                    w->color=x->parent->color;      //case4
                    x->parent->color=false;         //case4
                    w->right->color=false;          //case4
                    leftRotate(x->parent);          //case4
                    x=root;                         //case4
                }
            }
            else{
                w=x->parent->left;
                if(w->color==true){
                    w->color=false;                 //case1
                    x->parent->color=true;          //case1
                    rigthRotate(x->parent);         //case1
                    w=x->parent->left;              //case1
                }
                if(w->right->color==false && w->left->color==false){
                    w->color=true;                  //case2
                    x=x->parent;                    //case2
                }
                else{
                    if(w->left->color==false){
                        w->right->color=false;          //case3
                        w->color=true;                  //case3
                        leftRotate(w);                  //case3
                        w=x->parent->left;              //case3
                    }
                    w->color=x->parent->color;      //case4
                    x->parent->color=false;         //case4
                    w->left->color=false;           //case4
                    rigthRotate(x->parent);         //case4
                    x=root;                         //case4
                }   
            }
        }
    }
};
int main(){
    RbTree r;
    r.Insert(11);
    r.Insert(14);
    r.Insert(15);
    r.Insert(2);
    r.Insert(7);
    r.Insert(1);
    r.Insert(5);
    r.Insert(8);
    r.Insert(4);
    r.visualizeTree(r.root,0);
    cout<<"--------------------------------------------------------------------------"<<endl;
    r.RBDelete(4);
    r.visualizeTree(r.root,0);

}