
Tenemos operaciones base tal que $* or +$

un input $s$ ligado con otro input entero $s'$ que determina el resultado de $s$ operando

infinity representa (???) no tengo ganas de pensarlo

= $ "rec"_s (i,j) = cases(
	{} &"si" s' = l and i = 0,
	infinity &"si" s' < l or s' = l and i > 0, 
	{"rec"(i,l-i) union {i},"rec"(i,l/i) union {i}} & "caso contrario",
) $