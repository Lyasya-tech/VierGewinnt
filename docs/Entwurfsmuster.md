# Verhaltensmuster Chain of Responsibility

## Problem:
Ein mit der Zeit gewachsenes Programm beinhaltet mittlerweile viele unterschiedliche Checks - ohne jegliche Struktur. Manche Checks wiederholen sich sogar an verschiedenen Programmstellen. Sie prüfen zwar für unterschiedliche Programmabläufe, der Check an sich ist aber der gleiche.

Das **„Chain of Responsibility“ Entwurfsmuster** gibt vor, die einzelnen Checks als sogenannte „Handler“ zu implementieren. Die Handler können hintereinander geschaltet werden. Besteht die Anfrage den ersten Check wird sie zum zweiten Check weitergegeben usw.. Besteht die Anfrage den Check nicht, wird sie abgelehnt und nicht weitergereicht. Dadurch, dass die danach kommenden Handler nicht bemüht werden müssen, erspart man sich Ressourcen.

![RespChain](chainOfResp.png)
 
Erst wenn alle Handler bestanden wurden, kommt die Anfrage zu ihrem eigentlichen Ziel. Ein weiterer Vorteil ist, dass man einen bestimmten Handler an verschiedenen Programmstellen aufrufen kann und somit nicht Code kopieren muss.

Man kann das Design Pattern aber auch andersherum verwenden, und zwar, dass jeder einzelne Handler gefragt wird, ob er mit dem Request etwas machen kann und letztendlich nur der Handler, für den die Anfrage bestimmt ist, diese auch bearbeitet.

