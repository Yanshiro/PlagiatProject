<?php

$output = shell_exec("py Plagiat.py 2>&1");

// énumération de chaque cas
$array = [1 => -2, 2 => -1, 3 => 0, 4 => 1, 5 => 2];

for ($i=1; $i<=5; $i++)
	// afficher les différentes vues en fonction de la valeur retournée dans la condition
    if (intval($output)==$array[$i]) 
    {
        switch ($output) {
            case -1:
            header('Location: Views/Bravo.html');
                break;
            case 1:
            header('Location: Views/Jackpot.html');
                break;
            case 2:
            header('Location: Views/SameScheme.html');
                break;
            case -2:
            header('Location: Views/Error.html');
                break;
            case 0:
            header('Location: Views/DifferentSignature.html');
                break;
        }
    }

