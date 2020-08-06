# PrairieLearn
Nodarbībā Nr.16 es iepazinos ar PrairieLearn vidi.  
Pēc vides installēšanas, mēs varam sākt strādāt. Pirmkārt, vajag palaist vidi, piemēram ar komandu:  
>  
> sudo docker run -it --rm -p 3000000 prairielearn/prairielearn  
>  
Kad vide ir palaista, mēs varam tai piekļaut ar:
>  
> localhost:3000/pl  
>  
Mums automātiski būs administratora privilēģijas ar kuram mēs varam izveidot jaunas tēmas, jautājumu, testus vai eksāmenus. Pēc pirmas palaišanas vide bija papildināta ar automatizētiem testēšanas kursiem. Vide apskatīsies dažādi studentam un pasniedzējam. Tā vide apskatīsies pasniedzējam:  
>  
![INST_PRAIRE_VIEW](Pictures/INST_PRAIRE_VIEW.png)
>  
Tā vide apskatīsies studentam:  
>  
![STUD_PRAIRIE_VIEW](Pictures/STUD_PRAIRIE_VIEW.png)
>  
Arī pasniedzējs var redzēt studenta tēmas izpildīšanas procentuāli:  
>  
![GRADEBOOK_EXAMPLE](Pictures/GRADEBOOK_EXAMPLE.png)
>  
## Jaunas tēmas un uzdevuma izveidošana
Pēc jaunas tēmas un uzdevuma izveidošanas, vajag papildināt tēmu ar uzdevumu, kuru mēs jau izveidojam:  
>  
![QUEST_ASSESS_ADD](Pictures/QUEST_ASSESS_ADD.png)
>  
Kad es izveidoju jaunu uzdevumu, uzdevumā parādās automātiskik izveidotais uzdevums. Es viņu nemainīju, pamainīju tikai tekstu, lai tās būtu uzrakstīts latviski:  
>  
![QUEST_PIEM](Pictures/QUEST_PIEM.png)
>  
Lai uzdevums strādātu ir izveidots fails server.py, kur jau ir uzrakstīts uzdevuma kods (ģenerēt 2 random ciparus no 5 līdz 10, summēt tos un pareizu atbildi ienest 'correct_answers'):  
>  
![QUEST_SERVER_PIEM](Pictures/QUEST_SERVER_PIEM.png)
>  
Galu galā students redzēs jaunu tēmu un uzdevumu šādi:  
>  
![STUD_NEW_ASS_VIEW](Pictures/STUD_NEW_ASS_VIEW.png)
>  
>  
![STUD_NEW_QUEST_VIEW](Pictures/STUD_NEW_QUEST_VIEW.png)
>  
