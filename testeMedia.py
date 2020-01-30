import timeit
import statistics
temposCython = []
temposPython = []

for i in range(50):
    cython = timeit.timeit("bs_avg_cy.teste(10,20",
                           setup= 'import bs_avg_cy',
                           number = 1)

    python = timeit.timeit("bs_avg_cy.teste(10,20",
                           setup= 'import bs_avg_py',
                           number = 1)
    print("\nCython demorou {}s".format(cython))
    print("python demorou {}s\n\n".format(cython))
    temposCython.append(cython)
    temposPython.append(python)
print("\nMedia Iteração cython ::{}s".format(statistics.mean(temposCython)))
print("Media Iteração python ::{}s".format(statistics.mean(temposPython)))
print("cyton é  {}x mais rapido".format(statistics.mean(temposPython) / statistics.mean(temposCython)))