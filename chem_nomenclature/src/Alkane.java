import java.util.Arrays;

import processing.core.PApplet;

public class Alkane extends PApplet {
	alkane a;
	boolean flip[];
	public void setup() {
		size(600,600);
		a=new alkane(8,3,3);
		flip=new boolean[3];
		System.out.println(a);
		randBool(flip);
		//for (int i=1; i<=a.n; i++) System.out.println(i+" "+a.endTo(i)+" "+a.startTo(i));
	}
	String names[]={"methane","ethane","propane","butane","pentane","hexane","heptane","octane","nonane","decane"};
	String subNames[]={"methyl", "ethyl", "propyl", "butyl", "pentyl"}; //1,2,3,4,5
	public void draw() {
		background(0);
		fill(0,245,95);
		textSize(14);
		int k=0;
		String s=names[a.longestChain-1];
		if (a.subPositions.length>0) {
			boolean left=false;
			if (a.subPositions[0]%100<(a.n-a.subPositions[a.subPositions.length-1]%100)+1) {
				left=true;
			}
			boolean b=false;
				int v[]=a.getSubs(3);
				if (v!=null) {
					s=convert(v,subNames[2],left,a.n)+s;
					b=true;
				}
				v=a.getSubs(5);
				if (v!=null) {
					s=convert(v,subNames[0],left,a.n)+(b?"-":"")+s;
					b=true;
				}
				v=a.getSubs(1);
				if (v!=null) {
					s=convert(v,subNames[0],left,a.n)+(b?"-":"")+s;
					b=true;
				}
				v=a.getSubs(2);
				if (v!=null) {
					s=convert(v,subNames[1],left,a.n)+(b?"-":"")+s;
					b=true;
				}
				v=a.getSubs(4);
				if (v!=null) {
					s=convert(v,subNames[3],left,a.n)+(b?"-":"")+s;
				}
		}
		text(s,50,50);
		int p=width/2-(a.n*20);
		for (int i=1; i<=a.n; i++) {
			if (k<a.subPositions.length) {
				int m = a.subPositions[k];
				if (i== m%100) {
					m /= 100;
					if (flip[k]) {
						for (int r=1; r<=m; r++) {						
							text("|",p+4,height/2-28*r+14);
							text("C",p,height/2-28*r);
						}
					} else {
						for (int r=1; r<=m; r++) {						
							text("|",p+4,height/2+28*r-14);
							text("C",p,height/2+28*r);
						}

					}
					k++;
				}
			}
			if (i!=a.n) {
				text("C -- ",p,height/2);
				p+=40;
			} else text("C",p,height/2);

		}
	}
	private String convert(int[] v, String string, boolean left, int longest) {
		if (!left) {
			for (int i=0; i<v.length; i++) v[i]=longest-v[i]+1;
			Arrays.sort(v);
		}
		String s=Arrays.toString(v);
		s=s.substring(1,s.length()-1)+"-";
		if (v.length==2) s+="di";
		if (v.length==3) s+="tri";
		if (v.length==4) s+="tetra";
		if (v.length==5) s+="penta";
		if (v.length==6) s+="hexa";
		return s+string;
	}
	//sets every element of an array of booleans to true/false randomly 
	public void randBool(boolean b[]) {
		for (int i=0; i<b.length; i++) b[i]=Math.random()>=0.5;
	}
	public void keyPressed() {
		a=new alkane(8,3,3);
		System.out.println(a);
		randBool(flip);
	}

	public class alkane {
		int longestChain;
		int maxSubLength;
		int subPositions[];    //length*100 + position (1-origin)
		int n;
		//right now he passes a longest chain, number of subsituents, & the max length
		public alkane(int longestChain, int noSubs, int maxSubLength) {
			this.longestChain=longestChain;
			subPositions=new int[noSubs];
			this.maxSubLength=maxSubLength;
			//must be one C at each end otherwise sub is not a sub
			while (true) {
				int j=1;
				for (int i=0; i<noSubs; i++) {
					j+=(int) random(1,longestChain-noSubs-j);
					subPositions[i]=((int) random(1,maxSubLength+0.4f))*100+j;
				}
				int k;
				if (noSubs==0) k=1; else k=subPositions[noSubs-1]%100+1;
				for (n=k; n<=longestChain; n++)
					if (validate()==longestChain) return;
			}
		}
		public int[] getSubs(int no) {
			int x[]=new int[n];
			int k=0;
			for (int i=0; i<subPositions.length; i++) {
				if (subPositions[i]/100==no) x[k++]=subPositions[i]%100;
			}
			if (k==0) return null;
			int y[]=new int[k];
			System.arraycopy(x, 0, y, 0, k);
			return y;
		}
		public int validate() {
			int max = -1;
			for (int i=1; i<=n; i++) {
				int k=startTo(i);
				if (k>max) max=k;
				k=endTo(i);
				if (k>max) max=k;
			}
			for (int i=1; i<subPositions.length; i++) {
				for (int j=i+1; j<subPositions.length; j++) {
					int k=subTo(i,j);
					if (k>max) max=k;
				}
			}
			return max;
		}
		private int startTo(int i) {
			if (i<1 || i>n) throw new RuntimeException("bounds err "+this);
			for (int k=0; k<subPositions.length; k++) {
				int j=subPositions[k];
				if (i==j%100) return i+j/100;
			}
			return i;
		}
		private int endTo(int i) {
			if (i<1 || i>n) throw new RuntimeException("bounds err "+this);
			for (int k=0; k<subPositions.length; k++) {
				int j=subPositions[k];
				if (i<j%100) return n-i+1;
				if (i==j%100) return n-i+j/100+1;
			}
			return n-i+1;
		}
		private int subTo(int i, int j) {
			if (i<1 || i>n || i>=j) throw new RuntimeException("bounds err "+this);
			int m=subPositions[i-1];
			int p=subPositions[j-1];
			return p%100 - m%100+1 + p/100 + m/100;
		}
		public String toString() {
			return n+" "+longestChain+" "+Arrays.toString(subPositions);
		}
	}
}