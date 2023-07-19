class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        chemin = []
        path = path.split('/')
        for r in path:
            if r == ".." and len(chemin) != 0:
                chemin.pop()
            elif r != "." and r != '' and r != '..':
                chemin.append(r)

        return '/{}'.format('/'.join(chemin)) if len(chemin) != 0 else '/'

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
