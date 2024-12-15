questions = [

    "Q1. Which of the following states doesn’t share its boundary with Gujarat?🤔 \nA. Maharashtra \nB. Rajasthan \nC. Madhya Pradesh \nD. Goa",
    "Q2. According to Indian Mythology, Kans, the brother of Devaki was the ruler of which city?🤔 \nA Mathura \nB Dwarka \nC Indraprastha \nD Ujjain",
    "Q3. Who wrote the play “Romeo and Juliet”?🤔 \nA Oscar Wilde \nB William Shakespeare \nC Jane Austen \nD F. Scott Fitzgerald",
    "Q4. Who is the current Prime Minister of Canada?🤔 \nA Boris Johnson \nB Angela Merkel \nC Justin Trudeau \nD Emmanuel Macron",
    "Q5. Which state in India is also known as “Dev Bhoomi”?🤔 \nA Uttarakhand \nB Rajasthan \nC Himachal Pradesh \nD Arunachal Pradesh",
    "Q6. Which Indian Cricketer has the record for scoring the most number of ODI centuries?🤔\nA Sachin Tendulkar\nB Virat Kohli\nC Rohit Sharma\nD Rahul Dravid",
    "Q7. What is the name of the famous poet who wrote India’s national anthem “Jana Gana Mana”?🤔\nA Bankim Chandra Chattopadhyay\nB Rabindranath Tagore\nC Muhammad Iqbal\nD Sarojini Naidu",
    "Q8. The first ever full-length Gujarati movie is based on the life of which of the following personalities?🤔\nA Narsi Mehta\nB Premchand Bhatt\nC Mahatma Gandhi\nD Mira Bai",
    "Q9. Which of the following Prime ministers of India was born in present-day Gujarat?🤔\nA Chaudhary Charan Singh\nB Gulzarilal Nanda\nC Morarji Desai\nD Jawaharlal Nehru",
    "Q10. Which of the following Bollywood superstars lives in a Bungalow called Mannat?🤔\nA Salman Khan\nB Aamir Khan\nC Amitabh Bachchan\nD Shahrukh Khan"

     ]



def kbc(list_len=0, ans=0, rupee = 0):
    print(f'\n{questions[list_len]}')
    money = 1000 + int(rupee)      
    user_input = input("Enter the answer: ").title()
    if user_input == ans:
        print(f'{user_input} is correct answer. You got 🎉{money} rupees')
    elif user_input == 'Q':
        exit()    
    else:
        print(f'{user_input} is wrong. You got 0 rupees')
        print(f'Game Over. You earned {money - 1000} rupees')
        
        exit()

print('\nWelcome to KBC \nKaun Banega Crorepati \nPress "Q" to any time Quit.')

kbc(0, 'D')
kbc(1, 'A', 1000)
kbc(2, 'B', 2000)
kbc(3,'C', 3000)
kbc(4,'A',5000)
kbc(5,'B',10000)
kbc(6,'B',50000)
kbc(7,'A',1500000)
kbc(8,'C', 7000000)
print('\nlast question')
kbc(9, 'A',  9999000)
print('Jackpot! You become crorepati')

