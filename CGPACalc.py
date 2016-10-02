print('\t\t\tWelcome to the CGPA CALCULATOR')
input('\nPress the Enter key to continue and use it to enter data and display final results.')
input('NOTE: PLEASE BE READY WITH ALL YOUR MARKS BEFORE PRESSING THE ENTER KEY.')
while True:
    try:
        print('\nLet\'s begin with English...')
        print('Please enter your English UT-1 marks.')
        englishut1 = float(input())
        print('Now enter your English UT-2 marks.')
        englishut2 = float(input())
        print('And what about your English FA Activity 1 marks?')
        englishfa1 = float(input())
        print('Now enter your English FA Activity 2 marks...')
        englishfa2 = float(input())
        print('Looks like you still need to enter your FA Activity 3 marks.')
        englishfa3 = float(input())
        print('And finally your FA Activity 4 marks.')
        englishfa4 = float(input())
        print('Now finally add marks for your notebook. If it was 100% complete and checked on time, then give yourselves 20 marks or as told by your teacher. Otherwise put estimate on your notebook completion marks out of 20.')
        englishnb = float(input())
        englishsum = (englishut1 + englishut2 + englishfa1 + englishfa2 + englishfa3 + englishfa4 + englishnb) / 8
        print('Now finally enter your English exam marks (along with ASL added) to end.')
        englishexam = float(input())
        englishexam = englishexam / 3
        englishsum = englishsum + englishexam
        englishtrue = englishut1 + englishut2 + englishfa1 + englishfa2 + englishfa3 + englishfa4 + englishnb + englishexam
        english = englishsum * 2
        print('Your total score in English is ' + str(englishtrue) + ' marks and your percentage is ' + str(english) + '...')
        if (english >= 91) and (english <= 100):
            print('You got a deserving A1 in English! Congratulations!')
            english = 10
        elif (english >= 81) and (english < 91):
            print('You got a great A2 in English. After all you deserved it!')
            english = 9
        elif (english >= 71) and (english < 81):
            print('You got a good B1. Kep working hard like this!')
            english = 8
        elif (english >= 61) and (english < 71):
            print('Well, you got an average B2. That\'s good, but you can surely get better marks...')
            english = 7
        elif (english >= 51) and (english < 61):
            print('That\'s a not-at-all-good C1. Work HARDER.')
            english = 6
        elif (english >= 41) and (english < 51):
            print('STUDY Harder. C2 is not good AT ALL.')
            english = 5
        elif (english >= 33) and (english < 41):
            print('Phew! That was too close to failing! Thank goodness you got a D atleast. Why live at the border?')
            english = 4
        elif (english >= 21) and (english < 33):
            print('...And you have failed at E1. If you would have worked harder, you could have gone through with a pass...')
            english = 0
        elif (english >= 0) and (english < 21):
            print('...And you are out for a duck. You can only cry now, for you have got an E2!')
            english = 0
        else:
            print('Do you really think that I am a fool? The consequences of doing this WILL not be good beacause you have entered wrong data.')
            english = 0
        print('\nNow turn for your 2nd subject, your 2nd Language...')
        print('Please enter your 2nd Language UT-1 marks.')
        languageut1 = float(input())
        print('Now enter your 2nd Language UT-2 marks.')
        languageut2 = float(input())
        print('And what about your 2nd Language FA Activity 1 marks?')
        languagefa1 = float(input())
        print('Now enter your 2nd Language FA Activity 2 marks...')
        languagefa2 = float(input())
        print('Looks like you still need to enter your FA Activity 3 marks.')
        languagefa3 = float(input())
        print('And finally your FA Activity 4 marks.')
        languagefa4 = float(input())
        print('Now finally add marks for your notebook. If it was 100% complete and checked on time, then give yourselves 20 marks or as told by your teacher. Otherwise put estimate on your notebook completion marks out of 20.')
        languagenb = float(input())
        languagesum = (languageut1 + languageut2 + languagefa1 + languagefa2 + languagefa3 + languagefa4 + languagenb) / 8
        print('Now finally enter your 2nd Language exam marks to end.')
        languageexam = float(input())
        languageexam = languageexam / 3
        languagesum = languagesum + languageexam
        languagetrue = languageut1 + languageut2 + languagefa1 + languagefa2 + languagefa3 + languagefa4 + languagenb + languageexam
        language = languagesum * 2
        print('Your total score in 2nd Language is ' + str(languagetrue) + ' marks and your percentage is ' + str(language) + '...')
        if (language >= 91) and (language <= 100):
            print('You got a deserving A1 in 2nd Language! Congratulations!')
            language = 10
        elif (language >= 81) and (language < 91):
            print('You got a great A2 in 2nd Language. After all you deserved it!')
            language = 9
        elif (language >= 71) and (language < 81):
            print('You got a good B1. Kep working hard like this!')
            language = 8
        elif (language >= 61) and (language < 71):
            print('Well, you got an average B2. That\'s good, but you can surely get better marks...')
            language = 7
        elif (language >= 51) and (language < 61):
            print('That\'s a not-at-all-good C1. Work HARDER.')
            language = 6
        elif (language >= 41) and (language < 51):
            print('STUDY Harder. C2 is not good AT ALL.')
            language = 5
        elif (language >= 33) and (language < 41):
            print('Phew! That was too close to failing! Thank goodness you got a D atleast. Why live at the border?')
            language = 4
        elif (language >= 21) and (language < 33):
            print('...And you have failed at E1. If you would have worked harder, you could have gone through with a pass...')
            language = 0
        elif (language >= 0) and (language < 21):
            print('...And you are out for a duck. You can only cry now, for you have got an E2!')
            language = 0
        else:
            print('Do you really think that I am a fool? The consequences of doing this WILL not be good beacause you have entered wrong data.')
            language = 0
        print('\nNow turn for your 3rd subject, i.e. Maths...')
        print('Please enter your Maths UT-1 marks.')
        mathsut1 = float(input())
        print('Now enter your Maths UT-2 marks.')
        mathsut2 = float(input())
        print('And what about your Maths FA Activity 1 marks?')
        mathsfa1 = float(input())
        print('Now enter your Maths FA Activity 2 marks...')
        mathsfa2 = float(input())
        print('Looks like you still need to enter your FA Activity 3 marks.')
        mathsfa3 = float(input())
        print('And finally your FA Activity 4 marks.')
        mathsfa4 = float(input())
        print('Now finally add marks for your notebook. If it was 100% complete and checked on time, then give yourselves 20 marks or as told by your teacher. Otherwise put estimate on your notebook completion marks out of 20.')
        mathsnb = float(input())
        mathssum = (mathsut1 + mathsut2 + mathsfa1 + mathsfa2 + mathsfa3 + mathsfa4 + mathsnb) / 8
        print('Now finally enter your Maths exam marks to end.')
        mathsexam = float(input())
        mathsexam = mathsexam / 3
        mathssum = mathssum + mathsexam
        mathstrue = mathsut1 + mathsut2 + mathsfa1 + mathsfa2 + mathsfa3 + mathsfa4 + mathsnb + mathsexam
        maths = mathssum * 2
        print('Your total score in Maths is ' + str(mathstrue) + ' marks and your percentage is ' + str(maths) + '...')
        if (maths >= 91) and (maths <= 100):
            print('You got a deserving A1 in Maths! Congratulations!')
            maths = 10
        elif (maths >= 81) and (maths < 91):
            print('You got a great A2 in Maths. After all you deserved it!')
            maths = 9
        elif (maths >= 71) and (maths < 81):
            print('You got a good B1. Kep working hard like this!')
            maths = 8
        elif (maths >= 61) and (maths < 71):
            print('Well, you got an average B2. That\'s good, but you can surely get better marks...')
            maths = 7
        elif (maths >= 51) and (maths < 61):
            print('That\'s a not-at-all-good C1. Work HARDER.')
            maths = 6
        elif (maths >= 41) and (maths < 51):
            print('STUDY Harder. C2 is not good AT ALL.')
            maths = 5
        elif (maths >= 33) and (maths < 41):
            print('Phew! That was too close to failing! Thank goodness you got a D atleast. Why live at the border?')
            maths = 4
        elif (maths >= 21) and (maths < 33):
            print('...And you have failed at E1. If you would have worked harder, you could have gone through with a pass...')
            maths = 0
        elif (maths >= 0) and (maths < 21):
            print('...And you are out for a duck. You can only cry now, for you have got an E2!')
            maths = 0
        else:
            print('Do you really think that I am a fool? The consequences of doing this WILL not be good beacause you have entered wrong data.')
            maths = 0
        print('\nAnd now the 4th subject, which is Science.')
        print('Please enter your Science UT-1 marks.')
        scienceut1 = float(input())
        print('Now enter your Science UT-2 marks.')
        scienceut2 = float(input())
        print('And what about your Science FA Activity 1 marks?')
        sciencefa1 = float(input())
        print('Now enter your Science FA Activity 2 marks...')
        sciencefa2 = float(input())
        print('Looks like you still need to enter your FA Activity 3 marks.')
        sciencefa3 = float(input())
        print('And finally your FA Activity 4 marks.')
        sciencefa4 = float(input())
        print('Now finally add marks for your notebook. If it was 100% complete and checked on time, then give yourselves 20 marks or as told by your teacher. Otherwise put estimate on your notebook completion marks out of 20.')
        sciencenb = float(input())
        sciencesum = (scienceut1 + scienceut2 + sciencefa1 + sciencefa2 + sciencefa3 + sciencefa4 + sciencenb) / 8
        print('Now finally enter your Science exam marks to end.')
        scienceexam = float(input())
        scienceexam = scienceexam / 3
        sciencesum = sciencesum + scienceexam
        sciencetrue = scienceut1 + scienceut2 + sciencefa1 + sciencefa2 + sciencefa3 + sciencefa4 + sciencenb + scienceexam
        science = sciencesum * 2
        print('Your total score in Science is ' + str(sciencetrue) + ' marks and your percentage is ' + str(science) + '...')
        if (science >= 91) and (science <= 100):
            print('You got a deserving A1 in Science! Congratulations!')
            science = 10
        elif (science >= 81) and (science < 91):
            print('You got a great A2 in Science. After all you deserved it!')
            science = 9
        elif (science >= 71) and (science < 81):
            print('You got a good B1. Kep working hard like this!')
            science = 8
        elif (science >= 61) and (science < 71):
            print('Well, you got an average B2. That\'s good, but you can surely get better marks...')
            science = 7
        elif (science >= 51) and (science < 61):
            print('That\'s a not-at-all-good C1. Work HARDER.')
            science = 6
        elif (science >= 41) and (science < 51):
            print('STUDY Harder. C2 is not good AT ALL.')
            science = 5
        elif (science >= 33) and (science < 41):
            print('Phew! That was too close to failing! Thank goodness you got a D atleast. Why live at the border?')
            science = 4
        elif (science >= 21) and (science < 33):
            print('...And you have failed at E1. If you would have worked harder, you could have gone through with a pass...')
            science = 0
        elif (science >= 0) and (science < 21):
            print('...And you are out for a duck. You can only cry now, for you have got an E2!')
            science = 0            
        else:
            print('Do you really think that I am a fool? The consequences of doing this WILL not be good beacause you have entered wrong data.')
            science = 0
        print('\nAnd finally the last subject to end the calculations, S.St.')
        print('Please enter your S.St UT-1 marks.')
        sstut1 = float(input())
        print('Now enter your S.St UT-2 marks.')
        sstut2 = float(input())
        print('And what about your S.St FA Activity 1 marks?')
        sstfa1 = float(input())
        print('Now enter your S.St FA Activity 2 marks...')
        sstfa2 = float(input())
        print('Looks like you still need to enter your FA Activity 3 marks.')
        sstfa3 = float(input())
        print('And finally your FA Activity 4 marks.')
        sstfa4 = float(input())
        print('Now finally add marks for your notebook. If it was 100% complete and checked on time, then give yourselves 20 marks or as told by your teacher. Otherwise put estimate on your notebook completion marks out of 20.')
        sstnb = float(input())
        sstsum = (sstut1 + sstut2 + sstfa1 + sstfa2 + sstfa3 + sstfa4 + sstnb) / 8
        print('Now finally enter your S.St exam marks to end.')
        sstexam = float(input())
        sstexam = sstexam / 3
        sstsum = sstsum + sstexam
        ssttrue = sstut1 + sstut2 + sstfa1 + sstfa2 + sstfa3 + sstfa4 + sstnb + sstexam
        sst = sstsum * 2
        print('Your total score in S.St is ' + str(ssttrue) + ' marks and your percentage is ' + str(sst) + '...')
        if (sst >= 91) and (sst <= 100):
            print('You got a deserving A1 in S.St! Congratulations!')
            sst = 10
        elif (sst >= 81) and (sst < 91):
            print('You got a great A2 in S.St. After all you deserved it!')
            sst = 9
        elif (sst >= 71) and (sst < 81):
            print('You got a good B1. Kep working hard like this!')
            sst = 8
        elif (sst >= 61) and (sst < 71):
            print('Well, you got an average B2. That\'s good, but you can surely get better marks...')
            sst = 7
        elif (sst >= 51) and (sst < 61):
            print('That\'s a not-at-all-good C1. Work HARDER.')
            sst = 6
        elif (sst >= 41) and (sst < 51):
            print('STUDY Harder. C2 is not good AT ALL.')
            sst = 5
        elif (sst >= 33) and (sst < 41):
            print('Phew! That was too close to failing! Thank goodness you got a D atleast. Why live at the border?')
            sst = 4
        elif (sst >= 21) and (sst < 33):
            print('...And you have failed at E1. If you would have worked harder, you could have gone through with a pass...')
            sst = 0
        elif (sst >= 0) and (sst < 21):
            print('...And you are out for a duck. You can only cry now, for you have got an E2!')
            sst = 0
        else:
            print('Do you really think that I am a fool? The consequences of doing this WILL not be good beacause you have entered wrong data.')
            sst = 0
        if (english == 0) or (language == 0) or (maths == 0) or (science == 0) or (sst == 0):
            print('Unluckily, you flunked the examinations this time, and so you have no CGPA...')
        else:
            print('\n\nNow the time has come to reveal your CGPA...')
            input('...which is...')
            CGPA = float(english) + float(language) + float(maths) + float(science) + float(sst)
            CGPA = CGPA / 5
            print(str(CGPA) + ' CGPA!!!')
        print('I hope you liked this CGPA Calculator...')
        print('Would you like to calculate yours or your friend\'s CGPA again? Type \'Yes\' (without the quotation marks) to calculate CGPA again or press Enter to quit...')
        redo = input()
        if (redo == 'Yes') or (redo == 'yes') or (redo == 'YES') or (redo == 'yES'):
            print('OK then...\n\n')
            continue
        else:
            print('Bye. Talk to you later.')
            print('Thanks for downloading this CGPA Calculator. I hope you liked it.')
            input('Press enter to exit.')
        break
    except (ValueError, TypeError):
        input('Looks like you have entered wrong values... Press enter to try again.')
            

