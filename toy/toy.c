// http://twitter.com/maxtuno
#include <stdio.h>
#include <stdlib.h>

int eval() {
	char c;
	int n = 0, m = 0;
	char *cc = malloc(1024);
	fgets(cc, 1024, stdin);
	while ((c = *(cc++)) != '\n') {
		switch (c) {
		case '+':
			sscanf(cc++, "%i", &m);
			n += m;
			break;
		case '-':
			sscanf(cc++, "%i", &m);
			n -= m;
			break;
		case '*':
			sscanf(cc++, "%i", &m);
			n *= m;
			break;
		case '/':
			sscanf(cc++, "%i", &m);
			n /= m;
			break;
		default:
			break;
		}
	}
	return n;
}

int main() {
	for (;;) {
		printf(">> %i\n", eval());
	}
	return 0;
}