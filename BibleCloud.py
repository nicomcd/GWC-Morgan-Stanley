import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

genesis = ('''1In the beginning God created the
heavens and the earth.
2
Now the earth was formless and empty,
darkness was over the surface of the
deep, and the Spirit of God was
hovering over the waters.
3
And God said, "Let there be light," and
there was light.
4
God saw that the light was good, and
he separated the light from the darkness.
5
God called the light "day," and the
darkness he called "night." And there
was evening, and there was morningthe first day.
6
And God said, "Let there be an
expanse between the waters to
separate water from water."
7
So God made the expanse and
separated the water under the expanse
from the water above it. And it was so.
8
God called the expanse "sky." And
there was evening, and there was
morning-the second day.
9
And God said, "Let the water under the
sky be gathered to one place, and let
dry ground appear." And it was so.
10God called the dry ground "land," and
the gathered waters he called "seas."
And God saw that it was good.
11Then God said, "Let the land produce
vegetation: seed-bearing plants and
trees on the land that bear fruit with
seed in it, according to their various
kinds." And it was so.
12The land produced vegetation: plants
bearing seed according to their kinds
and trees bearing fruit with seed in it
according to their kinds. And God saw
that it was good.
13And there was evening, and there was
morning-the third day.
14And God said, "Let there be lights in
the expanse of the sky to separate the
day from the night, and let them serve
as signs to mark seasons and days and
years,
15and let them be lights in the expanse
of the sky to give light on the earth." And
it was so.
16God made two great lights-the greater
light to govern the day and the lesser
light to govern the night. He also made
the stars.
17God set them in the expanse of the
sky to give light on the earth,
18to govern the day and the night, and to
separate light from darkness. And God
saw that it was good.
19And there was evening, and there was
morning-the fourth day.
20And God said, "Let the water teem
with living creatures, and let birds fly
above the earth across the expanse of
the sky."
21So God created the great creatures of
the sea and every living and moving
thing with which the water teems,
according to their kinds, and every
winged bird according to its kind. And
God saw that it was good.
22God blessed them and said, "Be
fruitful and increase in number and fill
the water in the seas, and let the birds
increase on the earth."
23And there was evening, and there was
morning-the fifth day.
24And God said, "Let the land produce
living creatures according to their kinds:
livestock, creatures that move along the
ground, and wild animals, each
according to its kind." And it was so.
25God made the wild animals according
to their kinds, the livestock according to
their kinds, and all the creatures that
move along the ground according to
their kinds. And God saw that it was
good.
26Then God said, "Let us make man in
our image, in our likeness, and let them
rule over the fish of the sea and the
birds of the air, over the livestock, over
all the earth, and over all the creatures
that move along the ground."
27So God created man in his own image,
in the image of God he created him;
male and female he created them.
28God blessed them and said to them,
"Be fruitful and increase in number; fill
the earth and subdue it. Rule over the
fish of the sea and the birds of the air
and over every living creature that
moves on the ground."
29Then God said, "I give you every seedbearing plant on the face of the whole
earth and every tree that has fruit with
seed in it. They will be yours for food.
30And to all the beasts of the earth and
all the birds of the air and all the
creatures that move on the groundeverything that has the breath of life in
it-I give every green plant for food." And
it was so.
31God saw all that he had made, and it
was very good. And there was evening,
and there was morning-the sixth day.
2Thus the heavens and the earth were
completed in all their vast array.
2
By the seventh day God had finished
the work he had been doing; so on the
seventh day he rested from all his work.
3
And God blessed the seventh day and
made it holy, because on it he rested
from all the work of creating that he had
done.
4
This is the account of the heavens and
the earth when they were created.
When the Lord God made the earth and
the heavens5
and no shrub of the field had yet
appeared on the earth and no plant of
the field had yet sprung up, for the Lord
God had not sent rain on the earth and
there was no man to work the ground,
6
but streams came up from the earth
and watered the whole surface of the
ground7
the Lord God formed the man from the
dust of the ground and breathed into his
nostrils the breath of life, and the man
became a living being.
8
Now the Lord God had planted a
garden in the east, in Eden; and there
he put the man he had formed.
9
And the Lord God made all kinds of
trees grow out of the ground-trees that
were pleasing to the eye and good for
food. In the middle of the garden were
the tree of life and the tree of the
knowledge of good and evil.
10A river watering the garden flowed
from Eden; from there it was separated
into four headwaters.
11The name of the first is the Pishon; it
winds through the entire land of Havilah,
where there is gold.
12(The gold of that land is good;
aromatic resin and onyx are also there.)
13The name of the second river is the
Gihon; it winds through the entire land of
Cush.
14The name of the third river is the
Tigris; it runs along the east side of
Asshur. And the fourth river is the
Euphrates.
15The Lord God took the man and put
him in the Garden of Eden to work it and
take care of it.
16And the Lord God commanded the
man, "You are free to eat from any tree
in the garden;
17but you must not eat from the tree of
the knowledge of good and evil, for
when you eat of it you will surely die."
18The Lord God said, "It is not good for
the man to be alone. I will make a helper
suitable for him."
19Now the Lord God had formed out of
the ground all the beasts of the field and
all the birds of the air. He brought them
to the man to see what he would name
them; and whatever the man called
each living creature, that was its name.
20So the man gave names to all the
livestock, the birds of the air and all the
beasts of the field. But for Adam no
suitable helper was found.
21So the Lord God caused the man to
fall into a deep sleep; and while he was
sleeping, he took one of the man's ribs
and closed up the place with flesh.
22Then the Lord God made a woman
from the rib he had taken out of the man,
and he brought her to the man.
23The man said, "This is now bone of my
bones and flesh of my flesh; she shall
be called 'woman, ' for she was taken
out of man."
24For this reason a man will leave his
father and mother and be united to his
wife, and they will become one flesh.
25The man and his wife were both naked,
and they felt no shame.
3Now the serpent was more crafty
than any of the wild animals the Lord
God had made. He said to the woman,
"Did God really say, 'You must not eat
from any tree in the garden'?"
2
The woman said to the serpent, "We
may eat fruit from the trees in the
garden,
3
but God did say, 'You must not eat fruit
from the tree that is in the middle of the
garden, and you must not touch it, or
you will die.' "
4
"You will not surely die," the serpent
said to the woman.
5
"For God knows that when you eat of it
your eyes will be opened, and you will
be like God, knowing good and evil."
6
When the woman saw that the fruit of
the tree was good for food and pleasing
to the eye, and also desirable for
gaining wisdom, she took some and ate
it. She also gave some to her husband,
who was with her, and he ate it.
7
Then the eyes of both of them were
opened, and they realized they were
naked; so they sewed fig leaves
together and made coverings for
themselves.
8
Then the man and his wife heard the
sound of the Lord God as he was
walking in the garden in the cool of the
day, and they hid from the Lord God
among the trees of the garden.
9
But the Lord God called to the man,
"Where are you?"
10He answered, "I heard you in the
garden, and I was afraid because I was
naked; so I hid."
11And he said, "Who told you that you
were naked? Have you eaten from the
tree that I commanded you not to eat
from?"
12The man said, "The woman you put
here with me-she gave me some fruit
from the tree, and I ate it."
13Then the Lord God said to the woman,
"What is this you have done?" The
woman said, "The serpent deceived me,
and I ate."
14So the Lord God said to the serpent,
"Because you have done this, "Cursed
are you above all the livestock and all
the wild animals! You will crawl on your
belly and you will eat dust all the days of
your life.
15And I will put enmity between you and
the woman, and between your offspring
and hers; he will crush your head, and
you will strike his heel."
16To the woman he said, "I will greatly
increase your pains in childbearing; with
pain you will give birth to children. Your
desire will be for your husband, and he
will rule over you."
17To Adam he said, "Because you
listened to your wife and ate from the
tree about which I commanded you,
'You must not eat of it,' "Cursed is the
ground because of you; through painful
toil you will eat of it all the days of your
life.
18It will produce thorns and thistles for
you, and you will eat the plants of the
field.
19By the sweat of your brow you will eat
your food until you return to the ground,
since from it you were taken; for dust
you are and to dust you will return."
20Adam named his wife Eve, because
she would become the mother of all the
living.
21The Lord God made garments of skin
for Adam and his wife and clothed them.
22And the Lord God said, "The man has
now become like one of us, knowing
good and evil. He must not be allowed
to reach out his hand and take also from
the tree of life and eat, and live forever."
23So the Lord God banished him from
the Garden of Eden to work the ground
from which he had been taken.
24After he drove the man out, he placed
on the east side of the Garden of Eden
cherubim and a flaming sword flashing
back and forth to guard the way to the
tree of life.
4Adam lay with his wife Eve, and she
became pregnant and gave birth to Cain.
She said, "With the help of the Lord I
have brought forth a man."
2
Later she gave birth to his brother Abel.
Now Abel kept flocks, and Cain worked
the soil.
3
In the course of time Cain brought
some of the fruits of the soil as an
offering to the Lord .
4
But Abel brought fat portions from
some of the firstborn of his flock. The
Lord looked with favor on Abel and his
offering,
5
but on Cain and his offering he did not
look with favor. So Cain was very angry,
and his face was downcast.
6
Then the Lord said to Cain, "Why are
you angry? Why is your face downcast?
7
If you do what is right, will you not be
accepted? But if you do not do what is
right, sin is crouching at your door; it
desires to have you, but you must
master it."
8
Now Cain said to his brother Abel,
"Let's go out to the field." And while they
were in the field, Cain attacked his
brother Abel and killed him.
9
Then the Lord said to Cain, "Where is
your brother Abel?" "I don't know," he
replied. "Am I my brother's keeper?"
10The Lord said, "What have you done?
Listen! Your brother's blood cries out to
me from the ground.
11Now you are under a curse and driven
from the ground, which opened its
mouth to receive your brother's blood
from your hand.
12When you work the ground, it will no
longer yield its crops for you. You will be
a restless wanderer on the earth."
13Cain said to the Lord , "My punishment
is more than I can bear.
14Today you are driving me from the
land, and I will be hidden from your
presence; I will be a restless wanderer
on the earth, and whoever finds me will
kill me."
15But the Lord said to him, "Not so ; if
anyone kills Cain, he will suffer
vengeance seven times over." Then the
Lord put a mark on Cain so that no one
who found him would kill him.
16So Cain went out from the Lord 's
presence and lived in the land of Nod,
east of Eden.
17Cain lay with his wife, and she became
pregnant and gave birth to Enoch. Cain
was then building a city, and he named
it after his son Enoch.
18To Enoch was born Irad, and Irad was
the father of Mehujael, and Mehujael
was the father of Methushael, and
Methushael was the father of Lamech.
19Lamech married two women, one
named Adah and the other Zillah.
20Adah gave birth to Jabal; he was the
father of those who live in tents and
raise livestock.
21His brother's name was Jubal; he was
the father of all who play the harp and
flute.
22Zillah also had a son, Tubal-Cain, who
forged all kinds of tools out of bronze
and iron. Tubal-Cain's sister was
Naamah.
23Lamech said to his wives, "Adah and
Zillah, listen to me; wives of Lamech,
hear my words. I have killed a man for
wounding me, a young man for injuring
me.
24If Cain is avenged seven times, then
Lamech seventy-seven times."
25Adam lay with his wife again, and she
gave birth to a son and named him Seth,
saying, "God has granted me another
child in place of Abel, since Cain killed
him."
26Seth also had a son, and he named
him Enosh. At that time men began to
call on the name of the Lord .
5This is the written account of Adam's
line. When God created man, he made
him in the likeness of God.
2
He created them male and female and
blessed them. And when they were
created, he called them "man. "
3
When Adam had lived 130 years, he
had a son in his own likeness, in his
own image; and he named him Seth.
4
After Seth was born, Adam lived 800
years and had other sons and daughters.
5
Altogether, Adam lived 930 years, and
then he died.
6
When Seth had lived 105 years, he
became the father of Enosh.
7
And after he became the father of
Enosh, Seth lived 807 years and had
other sons and daughters.
8
Altogether, Seth lived 912 years, and
then he died.
9
When Enosh had lived 90 years, he
became the father of Kenan.
10And after he became the father of
Kenan, Enosh lived 815 years and had
other sons and daughters.
11Altogether, Enosh lived 905 years, and
then he died.
12When Kenan had lived 70 years, he
became the father of Mahalalel.
13And after he became the father of
Mahalalel, Kenan lived 840 years and
had other sons and daughters.
14Altogether, Kenan lived 910 years, and
then he died.
15When Mahalalel had lived 65 years, he
became the father of Jared.
16And after he became the father of
Jared, Mahalalel lived 830 years and
had other sons and daughters.
17Altogether, Mahalalel lived 895 years,
and then he died.
18When Jared had lived 162 years, he
became the father of Enoch.
19And after he became the father of
Enoch, Jared lived 800 years and had
other sons and daughters.
20Altogether, Jared lived 962 years, and
then he died.
21When Enoch had lived 65 years, he
became the father of Methuselah.
22And after he became the father of
Methuselah, Enoch walked with God
300 years and had other sons and
daughters.
23Altogether, Enoch lived 365 years.
24Enoch walked with God; then he was
no more, because God took him away.
25When Methuselah had lived 187 years,
he became the father of Lamech.
26And after he became the father of
Lamech, Methuselah lived 782 years
and had other sons and daughters.
27Altogether, Methuselah lived 969
years, and then he died.
28When Lamech had lived 182 years, he
had a son.
29He named him Noah and said, "He will
comfort us in the labor and painful toil of
our hands caused by the ground the
Lord has cursed."
30After Noah was born, Lamech lived
595 years and had other sons and
daughters.
31Altogether, Lamech lived 777 years,
and then he died.
32After Noah was 500 years old, he
became the father of Shem, Ham and
Japheth.
6When men began to increase in
number on the earth and daughters
were born to them,
2
the sons of God saw that the daughters
of men were beautiful, and they married
any of them they chose.
3
Then the Lord said, "My Spirit will not
contend with man forever, for he is
mortal ; his days will be a hundred and
twenty years."
4
The Nephilim were on the earth in
those days-and also afterward-when the
sons of God went to the daughters of
men and had children by them. They
were the heroes of old, men of renown.
5
The Lord saw how great man's
wickedness on the earth had become,
and that every inclination of the thoughts
of his heart was only evil all the time.
6
The Lord was grieved that he had
made man on the earth, and his heart
was filled with pain.
7
So the Lord said, "I will wipe mankind,
whom I have created, from the face of
the earth-men and animals, and
creatures that move along the ground,
and birds of the air-for I am grieved that
I have made them."
8
But Noah found favor in the eyes of the
Lord .
9
This is the account of Noah. Noah was
a righteous man, blameless among the
people of his time, and he walked with
God.
10Noah had three sons: Shem, Ham and
Japheth.
11Now the earth was corrupt in God's
sight and was full of violence.
12God saw how corrupt the earth had
become, for all the people on earth had
corrupted their ways.
13So God said to Noah, "I am going to
put an end to all people, for the earth is
filled with violence because of them. I
am surely going to destroy both them
and the earth.
14So make yourself an ark of cypress
wood; make rooms in it and coat it with
pitch inside and out.
15This is how you are to build it: The ark
is to be 450 feet long, 75 feet wide and
45 feet high.
16Make a roof for it and finish the ark to
within 18 inches of the top. Put a door in
the side of the ark and make lower,
middle and upper decks.
17I am going to bring floodwaters on the
earth to destroy all life under the
heavens, every creature that has the
breath of life in it. Everything on earth
will perish.
18But I will establish my covenant with
you, and you will enter the ark-you and
your sons and your wife and your sons'
wives with you.
19You are to bring into the ark two of all
living creatures, male and female, to
keep them alive with you.
20Two of every kind of bird, of every kind
of animal and of every kind of creature
that moves along the ground will come
to you to be kept alive.
21You are to take every kind of food that
is to be eaten and store it away as food
for you and for them."
22Noah did everything just as God
commanded him.
7The Lord then said to Noah, "Go into
the ark, you and your whole family,
because I have found you righteous in
this generation.
2
Take with you seven of every kind of
clean animal, a male and its mate, and
two of every kind of unclean animal, a
male and its mate,
3
and also seven of every kind of bird,
male and female, to keep their various
kinds alive throughout the earth.
4
Seven days from now I will send rain on
the earth for forty days and forty nights,
and I will wipe from the face of the earth
every living creature I have made."
5
And Noah did all that the Lord
commanded him.
6
Noah was six hundred years old when
the floodwaters came on the earth.
7
And Noah and his sons and his wife
and his sons' wives entered the ark to
escape the waters of the flood.
8
Pairs of clean and unclean animals, of
birds and of all creatures that move
along the ground,
9
male and female, came to Noah and
entered the ark, as God had
commanded Noah.
10And after the seven days the
floodwaters came on the earth.
11In the six hundredth year of Noah's life,
on the seventeenth day of the second
month-on that day all the springs of the
great deep burst forth, and the
floodgates of the heavens were opened.
12And rain fell on the earth forty days
and forty nights.
13On that very day Noah and his sons,
Shem, Ham and Japheth, together with
his wife and the wives of his three sons,
entered the ark.
14They had with them every wild animal
according to its kind, all livestock
according to their kinds, every creature
that moves along the ground according
to its kind and every bird according to its
kind, everything with wings.
15Pairs of all creatures that have the
breath of life in them came to Noah and
entered the ark.
16The animals going in were male and
female of every living thing, as God had
commanded Noah. Then the Lord shut
him in.
17For forty days the flood kept coming
on the earth, and as the waters
increased they lifted the ark high above
the earth.
18The waters rose and increased greatly
on the earth, and the ark floated on the
surface of the water.
19They rose greatly on the earth, and all
the high mountains under the entire
heavens were covered.
20The waters rose and covered the
mountains to a depth of more than
twenty feet. ,
21Every living thing that moved on the
earth perished-birds, livestock, wild
animals, all the creatures that swarm
over the earth, and all mankind.
22Everything on dry land that had the
breath of life in its nostrils died.
23Every living thing on the face of the
earth was wiped out; men and animals
and the creatures that move along the
ground and the birds of the air were
wiped from the earth. Only Noah was
left, and those with him in the ark.
24The waters flooded the earth for a
hundred and fifty days.
8But God remembered Noah and all
the wild animals and the livestock that
were with him in the ark, and he sent a
wind over the earth, and the waters
receded.
2
Now the springs of the deep and the
floodgates of the heavens had been
closed, and the rain had stopped falling
from the sky.
3
The water receded steadily from the
earth. At the end of the hundred and fifty
days the water had gone down,
4
and on the seventeenth day of the
seventh month the ark came to rest on
the mountains of Ararat.
5
The waters continued to recede until
the tenth month, and on the first day of
the tenth month the tops of the
mountains became visible.
6
After forty days Noah opened the
window he had made in the ark
7
and sent out a raven, and it kept flying
back and forth until the water had dried
up from the earth.
8
Then he sent out a dove to see if the
water had receded from the surface of
the ground.
9
But the dove could find no place to set
its feet because there was water over all
the surface of the earth; so it returned to
Noah in the ark. He reached out his
hand and took the dove and brought it
back to himself in the ark.
10He waited seven more days and again
sent out the dove from the ark.
11When the dove returned to him in the
evening, there in its beak was a freshly
plucked olive leaf! Then Noah knew that
the water had receded from the earth.
12He waited seven more days and sent
the dove out again, but this time it did
not return to him.
13By the first day of the first month of
Noah's six hundred and first year, the
water had dried up from the earth. Noah
then removed the covering from the ark
and saw that the surface of the ground
was dry.
14By the twenty-seventh day of the
second month the earth was completely
dry.
15Then God said to Noah,
16"Come out of the ark, you and your
wife and your sons and their wives.
17Bring out every kind of living creature
that is with you-the birds, the animals,
and all the creatures that move along
the ground-so they can multiply on the
earth and be fruitful and increase in
number upon it."
18So Noah came out, together with his
sons and his wife and his sons' wives.
19All the animals and all the creatures
that move along the ground and all the
birds-everything that moves on the
earth-came out of the ark, one kind after
another.
20Then Noah built an altar to the Lord
and, taking some of all the clean
animals and clean birds, he sacrificed
burnt offerings on it.
21The Lord smelled the pleasing aroma
and said in his heart: "Never again will I
curse the ground because of man, even
though every inclination of his heart is
evil from childhood. And never again will
I destroy all living creatures, as I have
done.
22"As long as the earth endures,
seedtime and harvest, cold and heat,
summer and winter, day and night will
never cease."
9Then God blessed Noah and his
sons, saying to them, "Be fruitful and
increase in number and fill the earth.
2
The fear and dread of you will fall upon
all the beasts of the earth and all the
birds of the air, upon every creature that
moves along the ground, and upon all
the fish of the sea; they are given into
your hands.
3
Everything that lives and moves will be
food for you. Just as I gave you the
green plants, I now give you everything.
4
"But you must not eat meat that has its
lifeblood still in it.
5
And for your lifeblood I will surely
demand an accounting. I will demand an
accounting from every animal. And from
each man, too, I will demand an
accounting for the life of his fellow man.
6
"Whoever sheds the blood of man, by
man shall his blood be shed; for in the
image of God has God made man.
7
As for you, be fruitful and increase in
number; multiply on the earth and
increase upon it."
8
Then God said to Noah and to his sons
with him:
9
"I now establish my covenant with you
and with your descendants after you
10and with every living creature that was
with you-the birds, the livestock and all
the wild animals, all those that came out
of the ark with you-every living creature
on earth.
11I establish my covenant with you:
Never again will all life be cut off by the
waters of a flood; never again will there
be a flood to destroy the earth."
12And God said, "This is the sign of the
covenant I am making between me and
you and every living creature with you, a
covenant for all generations to come:
13I have set my rainbow in the clouds,
and it will be the sign of the covenant
between me and the earth.
14Whenever I bring clouds over the earth
and the rainbow appears in the clouds,
15I will remember my covenant between
me and you and all living creatures of
every kind. Never again will the waters
become a flood to destroy all life.
16Whenever the rainbow appears in the
clouds, I will see it and remember the
everlasting covenant between God and
all living creatures of every kind on the
earth."
17So God said to Noah, "This is the sign
of the covenant I have established
between me and all life on the earth."
18The sons of Noah who came out of the
ark were Shem, Ham and Japheth.
(Ham was the father of Canaan.)
19These were the three sons of Noah,
and from them came the people who
were scattered over the earth.
20Noah, a man of the soil, proceeded to
plant a vineyard.
21When he drank some of its wine, he
became drunk and lay uncovered inside
his tent.
22Ham, the father of Canaan, saw his
father's nakedness and told his two
brothers outside.
23But Shem and Japheth took a garment
and laid it across their shoulders; then
they walked in backward and covered
their father's nakedness. Their faces
were turned the other way so that they
would not see their father's nakedness.
24When Noah awoke from his wine and
found out what his youngest son had
done to him,
25he said, "Cursed be Canaan! The
lowest of slaves will he be to his
brothers."
26He also said, "Blessed be the Lord ,
the God of Shem! May Canaan be the
slave of Shem.
27May God extend the territory of
Japheth ; may Japheth live in the tents
of Shem, and may Canaan be his
slave."
28After the flood Noah lived 350 years.
29Altogether, Noah lived 950 years, and
then he died.
10This is the account of Shem, Ham
and Japheth, Noah's sons, who
themselves had sons after the flood.
The Japhethites
2
The sons of Japheth: Gomer, Magog,
Madai, Javan, Tubal, Meshech and
Tiras.
3
The sons of Gomer: Ashkenaz, Riphath
and Togarmah.
4
The sons of Javan: Elishah, Tarshish,
the Kittim and the Rodanim.
5
(From these the maritime peoples
spread out into their territories by their
clans within their nations, each with its
own language.) The Hamites
6
The sons of Ham: Cush, Mizraim, Put
and Canaan.
7
The sons of Cush: Seba, Havilah,
Sabtah, Raamah and Sabteca. The
sons of Raamah: Sheba and Dedan.
8
Cush was the father of Nimrod, who
grew to be a mighty warrior on the earth.
9
He was a mighty hunter before the
Lord ; that is why it is said, "Like Nimrod,
a mighty hunter before the Lord ."
10The first centers of his kingdom were
Babylon, Erech, Akkad and Calneh, in
Shinar.
11From that land he went to Assyria,
where he built Nineveh, Rehoboth Ir,
Calah
12and Resen, which is between Nineveh
and Calah; that is the great city.
13Mizraim was the father of the Ludites,
Anamites, Lehabites, Naphtuhites,
14Pathrusites, Casluhites (from whom
the Philistines came) and Caphtorites.
15Canaan was the father of Sidon his
firstborn, and of the Hittites,
16Jebusites, Amorites, Girgashites,
17Hivites, Arkites, Sinites,
18Arvadites, Zemarites and Hamathites.
Later the Canaanite clans scattered
19and the borders of Canaan reached
from Sidon toward Gerar as far as Gaza,
and then toward Sodom, Gomorrah,
Admah and Zeboiim, as far as Lasha.
20These are the sons of Ham by their
clans and languages, in their territories
and nations. The Semites
21Sons were also born to Shem, whose
older brother was Japheth; Shem was
the ancestor of all the sons of Eber.
22The sons of Shem: Elam, Asshur,
Arphaxad, Lud and Aram.
23The sons of Aram: Uz, Hul, Gether
and Meshech.
24Arphaxad was the father of Shelah,
and Shelah the father of Eber.
25Two sons were born to Eber: One was
named Peleg, because in his time the
earth was divided; his brother was
named Joktan.
26Joktan was the father of Almodad,
Sheleph, Hazarmaveth, Jerah,
27Hadoram, Uzal, Diklah,
28Obal, Abimael, Sheba,
29Ophir, Havilah and Jobab. All these
were sons of Joktan.
30The region where they lived stretched
from Mesha toward Sephar, in the
eastern hill country.
31These are the sons of Shem by their
clans and languages, in their territories
and nations.
32These are the clans of Noah's sons,
according to their lines of descent,
within their nations. From these the
nations spread out over the earth after
the flood. ''')


wordcloud = WordCloud().generate(genesis)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
plt.savefig('genesis.png')
