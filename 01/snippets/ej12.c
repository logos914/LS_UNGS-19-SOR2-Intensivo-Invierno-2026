int fd = open("test.txt", O_CREAT | O_WRONLY,0644)

if (fd== -1 ) {
	perror("open");
	return 1;
} 
write (fd,"prueba",6)
close(fd);
