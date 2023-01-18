#include <iostream>
#include <string>

using namespace std;

int main()
{
	class Mahasiswa
	{
	public:
		string nama;
		string nim;
		double ipk;
		void setNama(string namaMahasiswa)
		{
			nama = namaMahasiswa;
		}

		void setNim(string nimMahasiswa)
		{
			nim = nimMahasiswa;
		}
		void setIpk(double ipkMahasiswa)
		{
			ipk = ipkMahasiswa;
		}
		string getNama()
		{
			return nama;
		}
		string getNim()
		{
			return nim;
		}
		double getIpk()
		{
			return ipk;
		}
	};
}