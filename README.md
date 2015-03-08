<h3>Bit-Castle---Game (V-2.2.5)</h3>
A Python (PyGame) based basic game

This is a simple game made using Python-2.7.9 (32-bit), PyGame and Tkinter. The application is for Windows System only.

<h3>INDEX</h3>
<ol>
<li><a href="#rulesandcontrols">Rules & Controls</a></li>
<li><a href="#windowssmartscreen">Windows Smart-Screen</a></li>
<li><a href="#requisites">Requisites</a></li>
<li><a href="#fixes">Fixes</a></li>
<li><a href="#execution">Installation & Execution</a></li>
<li><a href="#technologyused">Technology Used</a></li>
<li><a href="#testing">Testing</a></li>
<li><a href="#working">Working & GamePlay-Video</a></li>
</ol>

<a name="rulesandcontrols"><h3>1. Rules & Controls: </h3></a>
<ul>
<li>Goal of the game is to reach the door in each level.</li>
<li>Each level is completed only when the player REACHES THE GATE WITH THE KEY.</li>
<li>THE MORE BATTERY YOU SAVE, THE MORE YOU SCORE.</li>
<li>You have got a torch, it'll make it possible for you to see the objects in a level.</li>
<li>The torch can be turned OFF or ON using SPACE-BAR and cursor is moved using ARROW-KEYS.</li>
<li>When the torch is OFF, you can only see yourself and nothing else.</li>
<li>If the battery of the torch runs out, the torch is put-off automatically.</li>
<li>If you decide to put OFF the torch, the torch can be put back ON after a certain amout of time ONLY.</li>
<li>There are some 'red' colored crosses, touching them will kill you instantaneously.</li>
<li>There are some 'green' colored batteries, touching them will recharge your torch batteries a little.</li>
<li>You have to REACH THE GATE IN A CERTAIN AMOUNT OF TIME, else the Game Is Over.</li>
<li>After every level, you can visit the store and buy some boosts to help you in coming levels.</li>
<li>The left-over battery charge will be converted to coins at the end of any level.</li>
<li>Press Z to PAUSE.</li>
<li> Images used : 
<ul>
  <li><img src="https://raw.githubusercontent.com/pakhandi/Bit-Castle---Game/master/src/door.png"> --> Door </li>
  <li><img src="https://raw.githubusercontent.com/pakhandi/Bit-Castle---Game/master/src/key.png"> --> Key </li>
  <li><img src="https://raw.githubusercontent.com/pakhandi/Bit-Castle---Game/master/src/battery.PNG"> --> Recharge </li>
  <li><img src="https://raw.githubusercontent.com/pakhandi/Bit-Castle---Game/master/src/kill.png"> --> Death</li>
</ul>
</li>
</ul>

<a name="windowssmartscreen"><h3>2. Windows Smart Screen</h3></a>
To run the <b>bit_castle.exe</b> file you may need to bypass windows smartscreen warning.
<br>
<br>
<img src="https://raw.githubusercontent.com/pakhandi/Bit-Castle---Game/master/dist/win1.png">
<br>
<img src="https://raw.githubusercontent.com/pakhandi/Bit-Castle---Game/master/dist/win2.png">
<br>

<a name="requisites"><h3>3. Requisites</h3></a>
<ul>
<li>64-bit Windows System</li>
<li>Internet Connection</li>
</ul>

<a name="fixes"><h3>4. Fixes</h3></a>
<ul>
<li>Supports proxy connection for leaderboard updation (<b>dist/proxy.txt</b>)</li>
<li>Fixed png-chunk-length error</li>
</ul>

<a name="execution"><h3>5. Execution : </h3></a>
<ul>
<li> Download all the files from <a href="https://github.com/pakhandi/Bit-Castle---Game/archive/V-2.2.5.zip">here</a>.</li>
<li> Execute the <b>bit_castle.exe</b> file in the <b>dist</b> folder </li>
<li> If you are working behind proxy
	<ul>
	<li> Open <b>dist/proxy.txt</b></li>
	<li> Delete all the contents of the file and add your proxy with the following format
			<br>
		 <b>username:password@proxy:port</b>
	</li>
	</ul>
</li>
<li> Execute the <b>bitcastle.exe</b> file in the <b>dist</b> folder </li>
</ul>

<a name="technologyused"><h3>6. Technology Used</h3></a>
<ul>
<li>The game is made in Python-2.7.9</li>
<li>Pygame and Tkinter libraries</li>
<li>Executables were made using <b>py2exe</b></li>
</ul>

<a name="testing"><h3>7. Testing</h3></a>
The program has been tested on Windows-8.1(64-bit) and Windows-8.0(64-bit)..

<a name="working"><h3>8. Working</h3></a>
<a href="http://youtu.be/DigNsQLW4J8">GamePlay - Video</a><br>
When the Torch is ON : <br><br>
<img src="https://raw.githubusercontent.com/pakhandi/Bit-Castle---Game/master/dist/bitcastle_tut1.JPG">
<br>
<br>
When the Torch is OFF : <br><br>
<img src="https://raw.githubusercontent.com/pakhandi/Bit-Castle---Game/master/dist/bitcastle_tut2.JPG">
<br>
<br>
The working of the application is explained <a href="http://bugecode.com/post.php?pid=116">here</a>.
<br>

<span>For Hugs & Bugs, drop a mail at <b>asimkprasad@gmail.com</b></span>
