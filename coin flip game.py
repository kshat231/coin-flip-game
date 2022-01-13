from random import choice
def hot():
    print("Welcome to coin flip game")
    hotlist=["head", "tail"]
    head=str(input("Who choses head"))
    tail=str(input("Who choses tail"))
    while True:
        hot=choice(hotlist)
        if hot=="head":
            print(f"The coin flipped head! {head} wins")
        else:
            print(f"The coin flipped tails! {tail} wins")
        yn=str(input("Do you wanna play again (y/n)"))
        if yn=="y" or yn=="yes":
            print("Ok lets play again")
            continue
        else:
            print("Ok thanks a lot. Exited coin flip game!")
            break
if __name__=="__main__":
    hot()