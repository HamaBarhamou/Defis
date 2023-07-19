class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        chemin = []
        path_parts = path.split('/')

        for part in path_parts:
            if part == "..":
                if chemin:  # Vérifie si le chemin n'est pas vide avant de faire un pop
                    chemin.pop()
            elif part != "." and part != '' and part != '..':
                chemin.append(part)

        # Pas besoin de vérifier si le chemin est vide, join retourne une chaîne vide si la liste est vide
        return '/{}'.format('/'.join(chemin))

# Fonction principale pour tester le code
def main():
    solution = Solution()
    
    # Tester les cas limites
    print(solution.simplifyPath("/home/"))  # Doit imprimer "/home"
    print(solution.simplifyPath("/../"))  # Doit imprimer "/"
    print(solution.simplifyPath("/home//foo/"))  # Doit imprimer "/home/foo"
    print(solution.simplifyPath("/a/./b/../../c/"))  # Doit imprimer "/c"
    print(solution.simplifyPath("/../.."))  # Doit imprimer "/"
    print(solution.simplifyPath("/../../.."))  # Doit imprimer "/"
    print(solution.simplifyPath("/../../../.."))  # Doit imprimer "/"
    print(solution.simplifyPath("/a/../../b/../c//.//"))  # Doit imprimer "/c"

# Exécuter la fonction principale
if __name__ == "__main__":
    main()
