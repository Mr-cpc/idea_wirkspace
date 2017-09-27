package bupt_2017_9_26;

import myinterface.MultiwayTree;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;


/**
 * Created by waiting on 2017/9/25.
 */
public class Trie implements MultiwayTree{

    TrieNode root;

    /**
     * 构造一个空Trie
     */
    public Trie() {
        root = new TrieNode('\u0000',new ChildNode());
    }

    public Trie(TrieNode root) {
        this.root = new TrieNode('\u0000',new ChildNode());
        ChildNode cn = new ChildNode(root);
        root.firstChild.add(cn);
    }

    public void insert(String word) {
        TrieNode t = root,curChild = null;
        for(char c :word.toCharArray()) {
            curChild = t.hasChild(c);
            if(curChild != null) {
                t = curChild;
            }
            else {
                t = t.addChild(c);
            }
        }
        t.isWordEnd = true;
    }
    public boolean startsWith(String prefix) {
        TrieNode t = root,curChild = null;
        for(char c:prefix.toCharArray()) {
            curChild = t.hasChild(c);
            if(curChild != null)
                t = curChild;
            else
                return false;
        }
        return true;
    }
    public boolean search(String word) {
        TrieNode t = root,curChild = null;
        for (char c:word.toCharArray()) {
            curChild = t.hasChild(c);
            if(curChild != null)
                t = curChild;
            else
                return false;
        }
        return t.isWordEnd;
    }
    public boolean regSearch(String word) {
        List<Status> initialStatus = new ArrayList<>();;
        initialStatus.add(new Status(root));
        int i = 0;
        while(initialStatus.size() != 0 && i < word.length()) {
            List<Status> nextStatuses = new LinkedList<Status>();
            for(Status status:initialStatus) {
                List<Status> transferStatuses = status.transfer(word.charAt(i));
                nextStatuses.addAll(transferStatuses);
            }
            initialStatus.clear();
            initialStatus.addAll(nextStatuses);
            ++i;
        }
        return i == word.length() && initialStatus.iterator().next().trieNode.isWordEnd;
    }
    public static void main(String[] args) {
        Trie trie = new Trie();
        trie.insert("hello");
        trie.insert("world");
        trie.insert("hi");
        System.out.println(trie.regSearch(".e..o"));
    }
}

class TrieNode {
    char date;
    ChildNode firstChild;
    boolean isWordEnd;

    public TrieNode(char date, ChildNode firstChild) {
        this.date = date;
        this.firstChild = firstChild;
    }

    /**
     *
     * @param date
     * @return 返回parent
     */
    public TrieNode addChild(char date) {
        TrieNode child = new TrieNode(date,new ChildNode());//始终有一个no data的head
        ChildNode cn = new ChildNode(child);
        this.firstChild.add(cn);
        return child;
    }
    public void addChild(TrieNode child) {
        ChildNode cn = new ChildNode(child);
        this.firstChild.add(cn);
    }
    public TrieNode hasChild(char c) {
        ChildNode t = firstChild.next;
        while(t != null) {
            if(t.child.date == c)
                return t.child;
            else
                t = t.next;
        }
        return null;
    }

    public List<TrieNode> getAllChild() {
        ChildNode cur = this.firstChild.next;
        List<TrieNode> res = new ArrayList<>();
        while (cur != null) {
            res.add(cur.child);
            cur = cur.next;
        }
        return res;
    }
}

class ChildNode {
    TrieNode child ;
    ChildNode next;

    public ChildNode() {
    }

    public ChildNode(TrieNode child) {
        this.child = child;
    }

    public void add(ChildNode node) {
        ChildNode next = this.next;
        this.next = node;
        node.next = next;
    }

}


class Status {
    TrieNode trieNode;

    public Status(TrieNode trieNode) {
        this.trieNode = trieNode;
    }

    public List<Status> transfer(char c) {

        ChildNode cn = trieNode.firstChild.next;

        List<Status> res = new ArrayList<>();
        if(c == '.') {
            while (cn != null) {
                res.add(new Status(cn.child));
                cn = cn.next;
            }
        }
        else {
            while (cn != null) {
                if(cn.child.date == c) {
                    res.add(new Status(cn.child));
                    break;
                }
                else
                    cn = cn.next;
            }
        }
        return res;
    }

}
