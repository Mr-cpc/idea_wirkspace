package bupt_2017_9_27;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by waiting on 2017/9/27.
 */
public class MapSum {
    /*by jdk's Map---------*/
//    Map<String,Integer> map = new HashMap<>();
//    public void insert(String str,Integer i) {
//        map.put(str,i);
//    }
//    public int sum(String prefix) {
//        int res = 0;
//        for (Map.Entry<String, Integer> me : map.entrySet()) {
//            String value = me.getKey();
//            if(value.startsWith(prefix))
//                res += me.getValue();
//        }
//        return res;
//    }
    /*by jdk's Map END---------*/


    /*by self's Trie---------*/
    Trie trie = new Trie();
    public void insert(String str,Integer i) {
        trie.insert(str,i);
    }
    public int sum(String prefix) {
        TrieNode t = trie.startsWith(prefix);
        return t == null?0:t.num;
    }



    private static class Trie {
        TrieNode root;

        public Trie() {
            this.root = new TrieNode('\u0000',new ChildNode());
        }

        public void insert(String str, Integer i) {
            TrieNode t = root;
            for(char c:str.toCharArray()) {
                TrieNode cur = t.hasChild(c);
                if(cur != null)
                    t = cur;
                else {
                    t = t.addChild(c);
                }
                t.num+=i;
            }
            t.num += i;
            t.isWordEnd = true;
        }
        public TrieNode startsWith(String prefix) {
            TrieNode t = root;
            for (char c:prefix.toCharArray()) {
                TrieNode cur = t.hasChild(c);
                if(cur != null)
                    t = cur;
                else
                    return null;
            }
            return t;
        }
    }
    private static class TrieNode {
        char data;
        ChildNode firstChild;
        boolean isWordEnd;
        int num;

        public TrieNode(char data,ChildNode firstChild) {
            this.firstChild = firstChild;
            this.data = data;
        }

        public TrieNode hasChild(char c) {
            ChildNode firstChild = this.firstChild.next;
            while (firstChild != null) {
                if(firstChild.child.data == c)
                    return firstChild.child;
                else
                    firstChild = firstChild.next;
            }
            return null;
        }

        public TrieNode addChild(char c) {
            TrieNode child = new TrieNode(c,new ChildNode());
            ChildNode childNode = new ChildNode(child);
            this.firstChild.add(childNode);
            return child;

        }
    }
    private static class ChildNode {
        TrieNode child;
        ChildNode next;

        public ChildNode(TrieNode child) {
            this.child = child;
        }

        public ChildNode() {

        }


        public void add(ChildNode node) {
            ChildNode next = this.next;
            this.next = node;
            node.next = next;
        }

    }
    /*by self's Trie END---------*/
    public static void main(String[] args) {
        MapSum mapSum = new MapSum();
        mapSum.insert("apple",3);
        System.out.println(mapSum.sum("ap"));
        mapSum.insert("app",2);
        System.out.println(mapSum.sum("ap"));
    }
}
