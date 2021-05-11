def main():

  word = input("Ingresa una palabra: ")
  
  def is_palindromic(word: str):
    word = word.replace(' ', '')
    word = word.lower()
    word_reverse = word[::-1]
    if word == word_reverse:
      return True
    else:
      return False

  if is_palindromic(word) == True:
    print("Si es palindroma")
  else:
    print("No es palindroma")

if __name__ == "__main__":
  main()