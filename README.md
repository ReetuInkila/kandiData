# kandiData
Kanditaatin tutkielmani tarkoituksena on mallintaa spin-kubitin ja mekaanisen värähtelijän välistä kvanttimekaanista kytkentää. 
Simulaatioissa yksinkertaistan systeemin Jaynes--Cummings-mallia vastaavaksi, mikä on yksi esimerkki värähtelijän ja kaksitasoisen hiukkasen välisestä vuorovaikutuksesta. 
Tarkastelen systeemin mekaanisen resonanssin muutosta, sen kytkentää ja kvanttitilojen häviämisnopeuksia kuvaavien parametrien funktiona. 
Systeemin mallinnuksen tavoitteena on määrittää, millä kvanttitilojen häviämisnopeuksilla ja systeemin mittausajan parametreilla mekaanisen värähtelijän värähtelytaajuudet mahdollistavat spin-tilan havaitsemisen. 
Numeerisen tarkastelun suoritan ohjelmointikieli Pythonin ja sen kvanttimekaanisiin simulaatioihin tarkoitetun QuTiP-paketin avulla.

## Tutkielman päätelmät tiivistettynä
Kun ympäristö vaikuttaa kvanttisysteemin tilaan, kvanttitilan dekoherenssi kasvaa ajan myötä. Tämä merkitsee sitä, että kubitin kvanttitila ei säilytä informaatiotaan loputtomasti. Kun haluamme havaita kubitin spin-tilan mekaanisen värähtelijän taajuuden muutoksesta, täytyy mittauksen olla tarpeeksi nopea. Näin kvanttitilan häviäminen ei ehdi vaikuttaa kubitin tilaan. Toisaalta pidemmällä mittauksella on mahdollista havaita pienempiä muutoksia mekaanisen värähtelijän taajuudessa. Optimaalisen mittausajan tutkimiseksi tein simulaation, jossa mekaanisen värähtelijän viivanleveys on laskettu mittausajan sekä spin-tilan häviämisnopeuden tulon funktiona.

Kuvaaja: ![Mekaaniseen värähtelijän resonanssitaajuuden muutos sen ominaistaajuudesta, siihen kytketyn kubitin spinin romahdusoperaattoreiden  ja mittausajan tulon funktiona.](g_df_500s.pdf)


Kuviosta voidaan nähdä resonanssitaajuuden lähestyvän kytkemättömän värähtelijän taajuutta, kun mittausajan sekä spin-tilan häviämisnopeuden tulo kasvaa yli sadantuhannen. Esimerkiksi jos systeemin mittausaika on 0.02 sekuntia, voimme havaita mekaanisessa värähtelijässä yli 0.05 kHz taajuusmuutokset. Kuvion mukaan tällä mittausajalla muutos mekaanisen värähtekijän taajuudessa olisi siis havaittavisa kun spin tilan häviämisnopeus on alle 5000 kHz.

On kuitenkin huomattava, että simulaatio ei täysin vastaa kokeellista tutkimusta, sillä kokeellisessa tutkimuksessa resonaattorin värähtelyamplitudi ei mittauksen edetessä vaimene, vaan muuttuu jatkuvan termisen ajon vaikutuksesta. Simulaatiossa resonaattorin autokorrelaatiofunktio vaimenee siis ajan kuluessa nollaan mutta sen saavutettuaan se pysyy muuttumattomana. Autokorrelaatiofunktiosta tehty nopea Fourier-muunnos ei huomioi pysähtynyttä värähtelijää ja tästä johtuen taajuuden muutos ei pienene odotetusti mittausajan sekä spin-tilan häviämisnopeuden tulon kasvaessa.
