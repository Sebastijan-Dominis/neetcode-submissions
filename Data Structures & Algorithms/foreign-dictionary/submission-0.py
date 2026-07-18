class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # For each character, which character can only come after
        ordering = {character: [] for word in words for character in word}

        # Fill in ordering (adjacency list)
        for i in range(len(words) - 1):
            # Check the neighboring words
            word1 = words[i]
            word2 = words[i+1]

            # Minimum length of the words we are checking
            minLen = min(len(word1), len(word2))

            # Edge case -> same prefix but longer word comes first -> not allowed
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            
            # Only add the first differing character, since that is how words are sorted
            for j in range(minLen):
                if word1[j] != word2[j]:
                    ordering[word1[j]].append(word2[j])
                    break
        
        # One set for all of the visited characters and one for the path we are currently
        # exploring at any given point
        visited, path = set(), set()

        # A list of characters for output, but in reverse order
        result = []

        # Dfs to explore all relations
        def dfs(character: str) -> bool:
            # Cycle detected -> return True and then ""
            if character in path:
                return True
            # Already checked this character -> ignore and move on
            if character in visited:
                return False
            
            # Bookkeeping
            path.add(character)
            visited.add(character)

            # The recursive part -> will return True if a cycle gets detected
            for follower in ordering[character]:
                if dfs(follower):
                    return True
            
            # Done with this character -> clean up the path set
            path.remove(character)

            # Add the character to the result list
            result.append(character)

            # No cycles detected -> return False
            return False

        # Check each character from the adjacency list for cycles
        # Characters get added to the result list in the process of doing so
        for character in ordering:
            if dfs(character):
                return ""

        # Reverse the result, since we did a topological sort with postorder dfs
        result.reverse()

        # Join the characters into a single string and return
        return "".join(result)